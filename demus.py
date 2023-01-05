from .libs import*


def get_denoiser(device="cuda"):
    # Use a pre-trained model
    separator = pretrained.get_model(name="mdx").models[3]
    separator.to(device)
    separator.eval()
    return separator


def run_denoiser(separator, path):
    mix, sr = torchaudio.load(str(path))
    src_rate = separator.samplerate  # 44100
    mix = mix.cuda()
    ref = mix.mean(dim=0)  # mono mixture
    mix = (mix - ref.mean()) / ref.std()
    mix = convert_audio(mix, src_rate, separator.samplerate, separator.audio_channels)

    # Separate
    with torch.no_grad():
        estimates = apply_model(separator, mix[None], overlap=0.25)[0]  # defalut 0.25

    estimates = estimates * ref.std() + ref.mean()  # estimates * std + mean
    return estimates[3].cpu().numpy()[0, ...],sr