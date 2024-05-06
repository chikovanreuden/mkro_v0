class Profile:
    profiles = [ ]
    current = 1
    max = 4
    def __init__(self, name):
        self.name = name
        Profile.profiles.append(self)
    def __repr__(self):
      return f"Profile('{self.name}')"
    @staticmethod
    def get_current_profile_binary():
        # bin( Profile.current )[2:].zfill( profile_binary )
        return '{message:{fill}{align}{width}}'.format(
            message = bin( Profile.current )[ 2: ],
            fill = '0',
            align ='>',
            width = Profile.max,
        )
    @staticmethod
    def next():
        if Profile.current == len( Profile.profiles ):
            Profile.current = 1
        else:
            Profile.current = Profile.current + 1
        return Profile.current