from datetime import date

D2Raids = ["Last Wish", "Garden of Salvation", "Deep Stone Crypt", "Vault of Glass", "Vow of the Disciple", "King's Fall", "Root of Nightmares", "Crota's End", "Salvation's Edge"]
D2Dungeons = ["Shattered Throne", "Pit of Heresy", "Prophecy", "Grasp of Avarice", "Duality", "Spire of the Watcher", "Ghosts of the Deep", "Warlord's Ruin", "Vesper's Host", "Sundered Doctrine"]
D2RaidsLen = len(D2Raids)
D2DungeonsLen = len(D2Dungeons)

past_date = date(2026, 9, 8)
present_date = date.today()

num_weeks_since_origin = (present_date-past_date).days//7

print(f"It has been {num_weeks_since_origin} weeks since this program was written. Using {num_weeks_since_origin} to determine the current position in the raid and dungeon lists.")

RaidPos1 = (4 + num_weeks_since_origin) % D2RaidsLen
RaidPos2 = (8 + num_weeks_since_origin) % D2RaidsLen
DungeonPos1 = (3 + num_weeks_since_origin) % D2DungeonsLen
DungeonPos2 = (7 + num_weeks_since_origin) % D2DungeonsLen

def updatePos():
    present_date = date.today()

    num_weeks_since_origin = (present_date-past_date).days//7

    RaidPos1 = (4 + num_weeks_since_origin) % D2RaidsLen
    RaidPos2 = (8 + num_weeks_since_origin) % D2RaidsLen
    DungeonPos1 = (3 + num_weeks_since_origin) % D2DungeonsLen
    DungeonPos2 = (7 + num_weeks_since_origin) % D2DungeonsLen
