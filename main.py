from win10toast import ToastNotifier

toast = ToastNotifier()


toast.show_toast("Notification", "Notification body", duration=20,icon_path="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/microsoft/94/eyes_1f440.png")
