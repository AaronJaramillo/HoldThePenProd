#####TEST PROFILE SHEET
from ProfileSheet import ProfileSheet as ps


def main():
	rig = ps()
	rig.profileGen("/songs/51798")

	print(rig.title)
	print(rig.artist)
	print(rig.writers)
	print(rig.description)
	print(rig.lyrics)
	print(rig.lexicalDiverity)
	print(rig.lexicalDensity)
	print(rig.mostCommon)
	print(rig.readability)
	print(rig.kincaid)


main()