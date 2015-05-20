import logging
import sys
import os
import re

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)


def get_win_doc_folder():
    import ctypes.wintypes

    csidl_personal = 5
    shgfp_type_current = 0
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(0, csidl_personal, 0, shgfp_type_current, buf)
    return buf.value


def game_util_folder():
    """

    :return:
    """
    platform = sys.platform
    logging.debug(platform)

    if platform == "win32":

        get_windows_version = sys.getwindowsversion()
        logging.debug(get_windows_version)

        my_documents = get_win_doc_folder()
        logging.debug(my_documents)

        if get_windows_version.major >= 6:
            return os.path.join(my_documents, "My Games", "StarConflict")
        else:
            return os.path.join(my_documents, "My Games", "StarConflict")

    elif platform == "linux":
        return os.path.join(os.path.expanduser("~"), ".local", "share", "starconflict")

    elif platform == "darwin":
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Star Conflict")


def get_logs_directories():
    """

    :return:
    """
    return [f for f in os.listdir(os.path.join(game_util_folder(), "logs")) if
            re.match('\d{4}\.\d{2}\.\d{2} \d{2}\.\d{2}\.\d{2}', f)]


def get_last_directory():
    """

    :return:
    """
    return os.path.join(game_util_folder(), "logs", sorted(get_logs_directories())[-1])


if __name__ == "__main__":
    logging.info(game_util_folder())
    logging.info(get_last_directory())
