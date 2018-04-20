
class ServerStatistics:
    """
    This class represents the state of a server at an instant relative to some gathered data
    """

    # number of memebers, online and offline at a given instant
    num_members = 0
    num_online = 0
    num_offline = 0

    # running total of messages since the first instant
    total_messages = 0
    # running total of messages sent since last instant
    num_messages = 0

    # statistics of each channel
    channels = None

    # other server instances table. This will show the state at different recorded instants
    statistics_recording = None

class ChannelStatistics:
    """
    This class reresents the state of a channel at an instant relative to some gathered data
    """

    # number of memebers, online and offline at a given instant
    num_members = 0
    num_online = 0
    num_offline = 0

    # running total of messages since the first instant
    total_messages = 0
    # running total of messages sent since last instant
    num_messages = 0
