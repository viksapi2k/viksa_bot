SPOTIFY_ID: str = ""
SPOTIFY_SECRET: str = ""

EMBED_COLOR = 0xFFE933  #replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = ('.webm', '.mp4', '.mp3', '.avi', '.wav', '.m4v', '.ogg', '.mov')

MAX_SONG_PRELOAD = 5  #maximum of 25

COOKIE_PATH = "/../config/cookies/cookies.txt" #DO NOT TOUCH

GLOBAL_DISABLE_AUTOJOIN_VC = False

VC_TIMEOUT = 600 #seconds
VC_TIMOUT_DEFAULT = True  #default template setting for VC timeout true= yes, timeout false= no timeout
ALLOW_VC_TIMEOUT_EDIT = True  #allow or disallow editing the vc_timeout guild setting


STARTUP_MESSAGE = "[DingoLingo] Запуск модуля..."
STARTUP_COMPLETE_MESSAGE = "[DingoLingo] Запуск завершён"

NO_GUILD_MESSAGE = 'Ошибка: Пожалуйста, присоединитесь к голосовому каналу или введите команду в чат'
USER_NOT_IN_VC_MESSAGE = "Ошибка: Пожалуйста, присоединитесь к активному голосовому каналу, чтобы использовать команды"
WRONG_CHANNEL_MESSAGE = "Ошибка: Пожалуйста, используйте настроенный командный канал"
NOT_CONNECTED_MESSAGE = "Ошибка: Бот не подключен ни к одному голосовому каналу"
ALREADY_CONNECTED_MESSAGE = "Ошибка: Уже подключен к голосовому каналу"
CHANNEL_NOT_FOUND_MESSAGE = "Ошибка: Не удалось найти канал"
DEFAULT_CHANNEL_JOIN_FAILED = "Ошибка: Не удалось присоединиться к голосовому каналу по умолчанию"
INVALID_INVITE_MESSAGE = "Ошибка: Неверная ссылка на приглашение"

ADD_MESSAGE= "" #brackets will be the link text

INFO_HISTORY_TITLE = "Играли треки:"
MAX_HISTORY_LENGTH = 10
MAX_TRACKNAME_HISTORY_LENGTH = 15

SONGINFO_UPLOADER = "Загрузил: "
SONGINFO_DURATION = "Длительность: "
SONGINFO_SECONDS = "с"
SONGINFO_LIKES = "Лайков: "
SONGINFO_DISLIKES = "Дизлайков: "
SONGINFO_NOW_PLAYING = "Сейчас играет"
SONGINFO_QUEUE_ADDED = "Добавлено в очередь"
SONGINFO_SONGINFO = "Инфо о треке"
SONGINFO_ERROR = "Ошибка: Неподдерживаемый сайт или контент с возрастными ограничениями."
SONGINFO_PLAYLIST_QUEUED = "Очередь на воспроизведение:page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "Неизвестно"

HELP_ADDBOT_SHORT = ""
HELP_ADDBOT_LONG = ""
HELP_CONNECT_SHORT = "Подключить бота к голосовому каналу."
HELP_CONNECT_LONG = "Подключает бота к голосовому каналу, в котором вы сейчас находитесь."
HELP_DISCONNECT_SHORT = "Отключить бота от голосового канала."
HELP_DISCONNECT_LONG = "Отключить бота от голосового канала и остановить звук."

HELP_SETTINGS_SHORT = ""
HELP_SETTINGS_LONG = ""

HELP_HISTORY_SHORT = "Показать историю треков."
HELP_HISTORY_LONG = "Показывает " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " последних треков."
HELP_PAUSE_SHORT = "Приостановить трек."
HELP_PAUSE_LONG = "Приостанавливает работу аудиоплеера. Воспроизведение можно продолжить с помощью команды ;resume."
HELP_VOL_SHORT = "Изменяет громкость, %."
HELP_VOL_LONG = "Изменяет громкость аудиоплеера. Аргумент указывает %, на который должна быть установлена громкость."
HELP_PREV_SHORT = "Вернуться на один трек назад."
HELP_PREV_LONG = "Вернуться на один трек назад."
HELP_RESUME_SHORT = "Продолжает воспроизведение."
HELP_RESUME_LONG = "Возобновляет работу аудиоплеера."
HELP_SKIP_SHORT = "Пропустить трек."
HELP_SKIP_LONG = "Пропускает текущий воспроизводимый трек и переходит к следующему элементу в очереди."
HELP_SONGINFO_SHORT = "Информация о текущем треке."
HELP_SONGINFO_LONG = "Показывает подробную информацию о воспроизводимом в данный момент трек и размещает ссылку на него."
HELP_STOP_SHORT = "Остановить трек."
HELP_STOP_LONG = "Остановка аудиоплеера и очистка очереди треков."
HELP_MOVE_LONG = ""
HELP_MOVE_SHORT = 'Перемещает трек по очереди.'
HELP_YT_SHORT = "Воспроизведение поддерживаемой ссылки или поиск на youtube."
HELP_YT_LONG = ("$p [ссылка/название видео/ключевые слова/ссылка на плейлист]")
HELP_PING_SHORT = "Понг!"
HELP_PING_LONG = "Проверка состояния ответа бота."
HELP_CLEAR_SHORT = "Очистить очередь."
HELP_CLEAR_LONG = "Очищает очередь и пропускает текущую песню."
HELP_LOOP_SHORT = "Зацикливание текущей воспроизводимой композиции, вкл/выкл."
HELP_LOOP_LONG = "Зацикливает текущую воспроизводимую композицию и блокирует очередь. Используйте команду еще раз, чтобы отключить повтор."
HELP_QUEUE_SHORT = "Показывает песни в очереди."
HELP_QUEUE_LONG = "Показывает количество треков в очереди, до 10."
HELP_SHUFFLE_SHORT = "Перемешать очередь."
HELP_SHUFFLE_LONG = "Случайная сортировка треков в текущей очереди."
HELP_CHANGECHANNEL_SHORT = "Изменить канал бота"
HELP_CHANGECHANNEL_LONG = "Изменить канал бота на канал VC, в котором вы находитесь."

ABSOLUTE_PATH = '' #do not modify