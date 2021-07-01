"""A video player class."""

from .video_library import VideoLibrary
import random
is_playing = False
old_video = None
video_playing = None
is_paused = False

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temporary_list = []

        for vid in videos:

            tags ="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            temporary_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        sorted_list = sorted(temporary_list)
        for x in sorted_list:
            print(x)


    def play_video(self, video_id):
        global is_playing
        global old_video
        global video_playing
        video_playing = self._video_library.get_video(video_id)
        if video_playing != None:
            title = video_playing.title

        if not video_playing :
            print(f"Cannot play video: Video does not exist")
        else:
            if is_playing is True :
                print(f"Stoping video: {old_video.title}")
                print(f"Playing video: {title}")
                old_video = video_playing.title
            else:
                print(f"Playing video: {title}")
                is_playing = True
                old_video = video_playing.title

    def stop_video(self):
        """Stops the current video."""
        global video_playing
        global is_playing
        if is_playing == True :
            print(f"Stopping video: {video_playing.title}")
            is_playing = False
        else:
            print(f"Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        global video_playing
        global old_video
        global is_playing
        videos = self._video_library.get_all_videos()
        video_playing = random.choice(videos)
        if is_playing == False:
            print(f"Playing video : {video_playing.title}")
            is_playing = True
            old_video = video_playing.title
        else:
            print(f"Stoping video : {old_video}")
            print(f"Playing video : {video_playing.title}")


    def pause_video(self):
        """Pauses the current video."""
        global video_playing
        global is_paused

        if is_playing == False:
            print(f"Cannot pause video: No video is playing")
        else:
            if is_paused == False:
                print(f"Pausing video: {video_playing.title}")
                is_paused = True
            else:
                print(f"Video allready paused: {video_playing.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        global is_paused
        global is_playing
        if is_playing == False:
            print(f"Cannot continue video: No video is currently playing")
        elif is_paused == False:
            print(f"Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video : {video_playing.title}")
            is_paused = False

    def show_playing(self):
        """Displays video currently playing."""
        global is_playing
        global is_paused
        global video_playing
        if is_playing != None:
            tags ="["
            for tag in video_playing.tags:
                tags = tags + tag + " "
            tags = tags + "]"
            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

        if is_playing == False:
            print("No video is currently playing")
        elif is_playing == True and is_paused == False:
            print(f"Currently playing: {video_playing.title} ({video_playing.video_id}) {tags}")
        else:
            print(f"Currently playing: {video_playing.title} ({video_playing.video_id}) {tags} - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
