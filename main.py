from pytube import YouTube
import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")


class YtDownloader(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("YT Downloader")
        self.geometry("550x300")
        self.resizable(False, False)
        self.radio_var = customtkinter.IntVar(value=0)

        # Textbox for a link

        self.linkbox = customtkinter.CTkEntry(
            master=self,
            width=450,
            height=45,
            border_width=0,
            corner_radius=30,
            fg_color="#FFFFFF",
            font=("Satoshi Light", 18),
            text_color="#4D4D4D",
            placeholder_text_color="#D9D9D9",
            placeholder_text="https://www.youtube.com/watch?v=o3hlFvnS68k",
        )
        self.linkbox.grid(row=0, column=0)
        self.linkbox.place(
            relx=0.5,
            rely=0.3,
            anchor=tkinter.CENTER
        )

        # Download button

        self.download_button = customtkinter.CTkButton(
            master=self,
            width=150,
            height=45,
            border_width=0,
            corner_radius=30,
            fg_color="#FF0000",
            hover_color="#CC0000",
            border_color="#FFFFFF",
            text_color="#FFFFFF",
            font=("Satoshi Light", 20),
            text="Download",
            command=self.download_file
        )
        self.download_button.place(
            relx=0.5,
            rely=0.55,
            anchor=tkinter.CENTER
        )

        # Radio buttons - video

        self.video_button = customtkinter.CTkRadioButton(
            master=self,
            radiobutton_height=20,
            radiobutton_width=20,
            fg_color="#CC0000",
            border_width_checked=6,
            border_width_unchecked=3,
            border_color="#FF0000",
            hover_color="#CC0000",
            text="Video",
            font=("Satoshi Bold", 20),
            text_color="#D9D9D9",
            variable=self.radio_var,
            value=1
        )
        self.video_button.place(
            relx=0.35,
            rely=0.1,
            anchor=tkinter.CENTER)

        # Radio buttons - audio

        self.audio_button = customtkinter.CTkRadioButton(
            master=self,
            radiobutton_height=20,
            radiobutton_width=20,
            fg_color="#CC0000",
            border_width_checked=6,
            border_width_unchecked=3,
            border_color="#FF0000",
            hover_color="#CC0000",
            text="Audio",
            font=("Satoshi Bold", 20),
            text_color="#D9D9D9",
            variable=self.radio_var,
            value=2
        )
        self.audio_button.place(
            relx=0.65,
            rely=0.1,
            anchor=tkinter.CENTER)

        # Progress bar

        self.progressbar = customtkinter.CTkProgressBar(
            master=self,
            width=350,
            height=15,
            corner_radius=15,
            fg_color="#800000",
            progress_color="#FF0000",
            orientation="horizontal",
            mode="determinate",
        )
        self.progressbar.place(
            relx=0.5,
            rely=0.75,
            anchor=tkinter.CENTER)
        self.progressbar.set(value=0)

        # Downloading complete notification

        self.complete_notification = customtkinter.CTkLabel(
            master=self,
            width=200,
            height=50,
            corner_radius=0,
            fg_color="transparent",
            text_color="#D9D9D9",
            font=("Satoshi Bold", 30),
            text=" "
        )
        self.complete_notification.place(
            relx=0.5,
            rely=0.875,
            anchor=tkinter.CENTER)

    # Obtaining link
    def get_a_youtube_downloader_link(self):
        link = self.linkbox.get()
        yt_video = YouTube(link)

        return yt_video

    # Downloading the files
    def download_audio(self):
        yt_video = self.get_a_youtube_downloader_link()

        audio_only = yt_video.streams.get_audio_only()
        audio_file = audio_only.download()

        return audio_file

    def download_video(self):
        yt_video = self.get_a_youtube_downloader_link()

        full_video = yt_video.streams.get_highest_resolution()
        video_file = full_video.download()

        return video_file

    # Downloading function

    def download_file(self):
        choice_var = self.radio_var.get()
        # self.progressbar.start()
        if choice_var == 1:
            self.download_video()
            # self.progressbar.stop()
            self.complete_notification.configure(text="Complete!")
        elif choice_var == 2:
            self.download_audio()
            # self.progressbar.stop()
            self.complete_notification.configure(text="Complete!")


# Working once code is started?
if __name__ == "__main__":
    yt_downloader = YtDownloader()
    yt_downloader.mainloop()
