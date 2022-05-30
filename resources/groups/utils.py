from .models import Group, Profile


def get_groups():
    profiles = Profile.query.join(Group).group_by(Group.id).all()
    groups = {}
    for profile in profiles:
        group_name = profile.group.name
        if group_name not in groups:
            groups[group_name] = [profile.person]
        else:
            groups[group_name].append(profile.person)
    return groups
