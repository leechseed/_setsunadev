#!/usr/bin/env python3
"""Complete manual keying of all 210 batch7 tropes."""

import json

# Load nodes
nodes_dict = {}
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\nodes.compact.txt", "r") as f:
    line_num = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        line_num += 1
        nodes_dict[str(line_num)] = line.split(" | ")[0]

# Load tropes
tropes_list = []
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\batch7.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(" | ")
        if len(parts) >= 2:
            tropes_list.append(parts[0])

# Complete manual mapping based on semantic analysis
# Format: slug -> (node_id, confidence)
# null -> (None, "low")
manual_map = {}

# Lines 1-50
manual_map.update({
    "SecretPetPlot": ("10", "high"),
    "SecretRelationship": ("14", "high"),
    "SecretTest": ("112", "high"),
    "SecretTestOfCharacter": ("112", "high"),
    "SecretlyDying": (None, "low"),
    "SeekingTheIntangible": ("1", "medium"),
    "SeekingUltimateStrength": ("1", "medium"),
    "SelectiveEnforcement": (None, "low"),
    "SendInTheSearchTeam": ("84", "high"),
    "SeparatedAtBirth": ("41", "medium"),
    "SequelHook": (None, "low"),
    "SequencingDeception": (None, "low"),
    "SerendipityShock": ("14", "medium"),
    "SerialKiller": ("51", "high"),
    "SeriesFauxnale": (None, "low"),
    "SeriesGoal": (None, "low"),
    "SetRightWhatOnceWentWrong": ("17", "medium"),
    "SettlingTheFrontier": ("2", "medium"),
    "SexAsRiteOfPassage": ("13", "medium"),
    "SexEqualsLove": ("14", "high"),
    "SexForServices": ("43", "medium"),
    "SexyManInstantHarem": ("8", "low"),
    "ShaggyDogStory": (None, "low"),
    "ShaveAndAHaircut": (None, "low"),
    "SheCleansUpNicely": ("12", "low"),
    "SheIsNotMyGirlfriend": ("14", "medium"),
    "ShipTease": ("14", "high"),
    "ShipwreckStart": ("5", "medium"),
    "ShockAndSwitchEnding": (None, "low"),
    "ShootTheShaggyDog": ("20", "high"),
    "ShowWithinAShow": (None, "low"),
    "ShutUpHannibal": ("58", "medium"),
    "ShutUpKiss": ("14", "high"),
    "SidekickGlassCeiling": (None, "low"),
    "SigningOffCatchPhrase": (None, "low"),
    "SinkOrSwimFatherhood": ("13", "medium"),
    "SinkingShipScenario": ("114", "high"),
    "SkippingSchool": ("10", "medium"),
    "SlapSlapKiss": ("14", "high"),
    "SleepCute": ("14", "low"),
    "SleepLearning": ("112", "low"),
    "SlowAndSteadyWinsTheRace": ("47", "high"),
    "SlumberPartyPloy": ("10", "high"),
    "SmallMindedVillain": ("20", "medium"),
    "SnicketWarningLabel": (None, "low"),
    "SnipeHunt": ("79", "high"),
    "SnowballingThreat": ("84", "medium"),
    "SnowedIn": ("5", "high"),
    "SoNearYetSoFar": ("113", "high"),
})

# Lines 51-100
manual_map.update({
    "SoOnceAgainTheDayIsSaved": (None, "low"),
    "SoWhatDoWeDoNow": (None, "low"),
    "SolemnEndingTheme": (None, "low"),
    "SomeoneToRememberHimBy": ("71", "high"),
    "SomethingWeForgot": (None, "low"),
    "SorcerersApprenticePlot": ("87", "medium"),
    "SouvenirLand": (None, "low"),
    "SpeakNowOrForeverHoldYourPeace": ("108", "high"),
    "SpeedDating": ("14", "low"),
    "SpellingBee": ("47", "low"),
    "SplitAndReunion": ("40", "medium"),
    "SplitTimelinesPlot": (None, "low"),
    "SpotTheImpostor": ("99", "high"),
    "StalkerShot": (None, "low"),
    "StandardHeroReward": ("106", "high"),
    "StartMyOwn": ("35", "medium"),
    "StartOfDarkness": ("20", "high"),
    "StartToCorpse": ("83", "high"),
    "StarterVillain": ("68", "medium"),
    "StarterVillainStays": ("68", "medium"),
    "StartsWithASuicide": ("51", "high"),
    "StartsWithTheirFuneral": ("71", "high"),
    "StepOneEscape": ("5", "high"),
    "SternChase": ("96", "high"),
    "StockClockHandHang": (None, "low"),
    "StockEvilOverlordTactics": ("83", "high"),
    "StockSeriesFinales": (None, "low"),
    "StockSitcomGrandFinale": (None, "low"),
    "StoneSoup": ("79", "high"),
    "StopTheHeroTwist": (None, "low"),
    "StormInATeacup": (None, "low"),
    "StormingTheCastle": ("116", "high"),
    "StorybookEpisode": (None, "low"),
    "StorybookOpening": (None, "low"),
    "StrangerBehindTheMask": ("99", "high"),
    "StrangerInAFamiliarLand": ("118", "medium"),
    "StrangerInAStrangeSchool": ("74", "high"),
    "StrangersOnATrainPlotMurder": ("35", "high"),
    "StuffBlowingUp": ("116", "medium"),
    "StumbledIntoThePlot": ("84", "high"),
    "StumblingUponTheLostWizard": ("87", "high"),
    "StylisticCallback": (None, "low"),
    "Suburbia": (None, "low"),
    "SubvertedSuspicionAesop": (None, "low"),
    "SuccessionCrisis": ("35", "high"),
    "SuddenDownerEnding": ("20", "high"),
    "SuddenIntelligence": ("12", "low"),
    "SuddenMusicalEnding": (None, "low"),
    "SugarApocalypse": ("31", "high"),
    "SuicidalCosmicTemperTantrum": ("51", "medium"),
    "SuicideMission": ("59", "high"),
})

# Lines 101-150
manual_map.update({
    "SummonEverymanHero": ("84", "high"),
    "SuperPowersForADay": ("89", "medium"),
    "SuperheroEpisode": (None, "low"),
    "SuperheroOrigin": ("107", "medium"),
    "SuperweaponSurprise": (None, "low"),
    "SupportingCharactersSayGoodbye": ("118", "medium"),
    "SurpriseParty": ("22", "low"),
    "SurprisinglyHappyEnding": ("19", "high"),
    "SurprisinglyMundaneReason": (None, "low"),
    "SurvivalThroughSelfSacrifice": ("59", "high"),
    "SurvivedTheBeginning": (None, "low"),
    "SuspicionAesop": (None, "low"),
    "SuspiciouslySpecificSermon": (None, "low"),
    "SwearWordPlot": (None, "low"),
    "SymbolicHeroRebirth": ("117", "high"),
    "SympatheticWithAddedContext": ("41", "medium"),
    "SystematicVillainTakedown": ("83", "high"),
    "TagAlongActor": ("87", "low"),
    "TagTeamSuicide": ("51", "high"),
    "TakeAThirdOption": (None, "low"),
    "TakeCareOfTheKids": ("56", "high"),
    "TakeMyHand": ("116", "medium"),
    "TakeOverTheCity": ("35", "high"),
    "TakeOverTheWorld": ("35", "high"),
    "TakeUpMySword": ("84", "high"),
    "TakeYourChildToWorkDayPlot": (None, "low"),
    "TakenDuringTheEnding": (None, "low"),
    "TakingOverHeaven": ("35", "high"),
    "TakingOverTheTown": ("35", "high"),
    "TalentContest": ("47", "high"),
    "TalkShowAppearance": (None, "low"),
    "TalkingYourWayOut": ("79", "high"),
    "TallTale": (None, "low"),
    "TeachHimAnger": ("52", "low"),
    "TeacherStudentRomance": ("15", "high"),
    "TechnicianVersusPerformer": ("27", "low"),
    "TenLittleMurderVictims": ("37", "high"),
    "ThatDidntHappen": (None, "low"),
    "ThatOneSummer": (None, "low"),
    "ThatsAllFolks": (None, "low"),
    "TheBGrade": (None, "low"),
    "TheBadGuyWins": ("20", "high"),
    "TheBardOnBoard": (None, "low"),
    "TheBet": ("27", "high"),
    "TheBigBadShuffle": (None, "low"),
    "TheBigDamnKiss": ("14", "high"),
    "TheBigRace": ("47", "high"),
    "TheBreakfastPlot": ("73", "high"),
    "TheBrideWithAPast": (None, "low"),
    "TheCakeIsALie": ("34", "high"),
})

# Lines 151-210
manual_map.update({
    "TheCallHasBadReception": ("108", "low"),
    "TheCallKnowsWhereYouLive": ("108", "high"),
    "TheCallLeftAMessage": ("108", "high"),
    "TheCallPutMeOnHold": ("108", "medium"),
    "TheCaper": ("37", "high"),
    "TheCaptivityNarrative": ("39", "high"),
    "TheCavalry": ("32", "high"),
    "TheCavalryArrivesLate": ("116", "high"),
    "TheChainOfHarm": ("6", "medium"),
    "TheChase": ("3", "high"),
    "TheChooserOfTheOne": ("109", "medium"),
    "TheCollector": ("27", "high"),
    "TheCon": ("79", "high"),
    "TheConspiracy": ("35", "high"),
    "TheConvenientStoreNextDoor": (None, "low"),
    "TheDayOfReckoning": ("114", "high"),
    "TheDogBitesBack": ("6", "high"),
    "TheDragonsComeBack": ("2", "medium"),
    "TheDulcineaEffect": ("14", "medium"),
    "TheEnd": (None, "low"),
    "TheEndOfTheBeginning": ("107", "high"),
    "TheEndOrIsIt": (None, "low"),
    "TheEndingChangesEverything": (None, "low"),
    "TheEvilsOfFreeWill": ("35", "high"),
    "TheFellowshipHasEnded": ("118", "medium"),
    "TheFinalTemptation": ("10", "high"),
    "TheFunInFuneral": (None, "low"),
    "TheGameNeverStopped": ("112", "medium"),
    "TheGamePlaysYou": ("10", "high"),
    "TheGlomp": ("14", "low"),
    "TheGoodGuysAlwaysWin": ("19", "high"),
    "TheGoodKingdom": ("107", "high"),
    "TheGreatRepair": ("37", "high"),
    "TheGreatestStoryNeverTold": ("118", "low"),
    "TheGrovel": ("14", "high"),
    "TheHero": ("107", "high"),
    "TheHeroDies": ("20", "high"),
    "TheHollywoodFormula": (None, "low"),
    "TheHomewardJourney": ("116", "high"),
    "TheIdolsBlessing": ("87", "high"),
    "TheInfiltration": ("79", "high"),
    "TheInspectorIsComing": ("112", "medium"),
    "TheJungleOpera": ("2", "medium"),
    "TheMagicComesBack": ("32", "high"),
    "TheMagicGoesAway": ("31", "high"),
    "TheMagnificentSevenSamurai": ("37", "high"),
    "TheMakeover": ("12", "high"),
    "TheManBehindTheCurtain": ("103", "high"),
    "TheMasochismTango": ("14", "low"),
    "TheMigration": ("2", "medium"),
    "TheMovingExperience": ("2", "medium"),
    "TheOneWhoMadeItOut": ("19", "high"),
    "TheOnlyOne": ("108", "high"),
    "ThePictureCameWithTheFrame": (None, "low"),
    "ThePromPlot": (None, "low"),
    "ThePromisedLand": ("108", "high"),
    "TheQueenWillBeWatching": ("112", "medium"),
    "TheQuest": ("1", "high"),
    "TheResolutionWillNotBeIdentified": (None, "low"),
    "TheReveal": (None, "low"),
})

# Build results
results = []
for slug in tropes_list:
    if slug in manual_map:
        node_id, conf = manual_map[slug]
    else:
        print(f"WARNING: {slug} not found, defaulting to null")
        node_id, conf = None, "low"

    results.append({
        "slug": slug,
        "node": node_id,
        "alt": None,
        "conf": conf
    })

# Write output
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\keys.batch7.json", "w") as f:
    json.dump(results, f, indent=2)

# Validate
keyed = sum(1 for r in results if r["node"] is not None)
null = len(results) - keyed
print(f"Wrote {len(results)} keys")
print(f"Keyed: {keyed}, Null: {null}")

# Check node IDs are valid
valid_ids = set(nodes_dict.keys())
errors = 0
for r in results:
    if r["node"] and r["node"] not in valid_ids:
        print(f"ERROR: Node {r['node']} invalid for {r['slug']}")
        errors += 1

if errors == 0:
    print("All node IDs valid!")
else:
    print(f"{errors} validation errors!")
