import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporter codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}")


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporter codec."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (baseline) format to {folder}")


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporter codec with Hi422P profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}")


class AudioExporter(ABC):
    """Basic representation of audio exporting codac."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepare audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exported codac."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export")

    def do_export(self, folder: pathlib.Path):
        print(f"Preparing audio data in AAC format to {folder}")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exported codac."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export")

    def do_export(self, folder: pathlib.Path):
        print(f"Preparing audio data in WAV format to {folder}")


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codacs.
    The factory doesn't maintain any of the instances it creates.
    """

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video eporter instance."""

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance."""


class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed, low quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a slow speed, high quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing a low speed, master quality export."""

    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }
    # read the desired quality
    while True:
        export_quality = input("Exter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unkown output quality option: {export_quality}")


def main() -> None:
    """Main function"""

    fac = read_exporter()

    # retrieve the video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("paceholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
