"""@desktop_sender(title="Knockknock Desktop Notifier")
def train_your_nicest_model(wait):
    import time
    time.sleep(wait)
    return {"loss": 0.9}"""

import os
import datetime
import traceback
import functools
import socket
import subprocess
import platform

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def desktop_sender(title: str = "Lupy notify"):
    def show_notification(text: str, title: str):
        # Check the OS
        if platform.system() == "Darwin":
            subprocess.run(["sh", "-c", "osascript -e 'display notification \"%s\" with title \"%s\"'" % (text, title)])

        elif platform.system() == "Linux":
            subprocess.run(["notify-send", title, text])

        elif platform.system() == "Windows":
            try:
                from win10toast import ToastNotifier
            except ImportError as err:
                print(
                    'Error: to use Windows Desktop Notifications, you need to install `win10toast` first. Please run `pip install win10toast==0.9`.')

            toaster = ToastNotifier()
            toaster.show_toast(title,
                               text,
                               icon_path=None,
                               duration=5)

    def decorator_sender(func):
        @functools.wraps(func)
        def wrapper_sender(*args, **kwargs):

            start_time = datetime.datetime.now()
            host_name = socket.gethostname()
            func_name = func.__name__

            # Handling distributed training edge case.
            # In PyTorch, the launch of `torch.distributed.launch` sets up a RANK environment variable for each process.
            # This can be used to detect the master process.
            # See https://github.com/pytorch/pytorch/blob/master/torch/distributed/launch.py#L211
            # Except for errors, only the master process will send notifications.
            if 'RANK' in os.environ:
                master_process = (int(os.environ['RANK']) == 0)
                host_name += ' - RANK: %s' % os.environ['RANK']
            else:
                master_process = True

            if master_process:
                contents = [f"{func_name} has started 🎬",
                            'Machine name: %s' % host_name,
                            'Starting date: %s' % start_time.strftime(DATE_FORMAT)]
                text = '\n'.join(contents)
                show_notification(text, title)

            try:
                value = func(*args, **kwargs)

                if master_process:
                    end_time = datetime.datetime.now()
                    elapsed_time = end_time - start_time
                    contents = [f"{func_name} is complete 🎉",
                                f"Training duration: {str(elapsed_time)}",
                                f"Machine name:  {host_name}",
                                f"Starting date: {start_time.strftime(DATE_FORMAT)}",
                                f"End date: {end_time.strftime(DATE_FORMAT)}",
                                ]

                    try:
                        str_value = str(value)
                        contents.append('Main call returned value: %s' % str_value)
                    except:
                        contents.append('Main call returned value: %s' % "ERROR - Couldn't str the returned value.")

                    text = '\n'.join(contents)
                    show_notification(text, title)

                return value

            except Exception as ex:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time
                contents = [f"{func_name} has crashed ☠️",
                            'Machine name: %s' % host_name,
                            "Here's the error:",
                            '%s\n\n' % ex,
                            "Traceback:",
                            '%s' % traceback.format_exc()]
                text = '\n'.join(contents)
                show_notification(text, title)
                raise ex

        return wrapper_sender

    return decorator_sender