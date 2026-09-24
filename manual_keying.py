#!/usr/bin/env python3
"""
Manual keying tool for batch7 tropes to master plot nodes.
Read each trope and assign the best matching node by judgment.
"""

import json

# Load nodes
nodes = {}
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\nodes.compact.txt", "r") as f:
    line_num = 0
    for line in f:
        line = line.strip()
        if not line:
            continue
        line_num += 1
        parts = line.split(" | ", 2)
        if len(parts) >= 2:
            node_id = str(line_num)
            structured_id = parts[0]
            title = parts[1]
            definition = parts[2] if len(parts) > 2 else ""
            nodes[node_id] = {
                "id": structured_id,
                "title": title,
                "def": definition[:80] + "..." if len(definition) > 80 else definition
            }

# Load tropes
tropes = []
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\batch7.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(" | ", 3)
        if len(parts) >= 2:
            tropes.append({
                "slug": parts[0],
                "name": parts[1],
                "def": parts[2] if len(parts) > 2 else "",
                "indexes": parts[3] if len(parts) > 3 else ""
            })

print(f"\nNodes available: {len(nodes)}")
print(f"Tropes to key: {len(tropes)}\n")

# Show node reference
print("=== MASTER PLOT NODES (Summary) ===")
print("\nTobias Jones (20 plots):")
for i in range(1, 21):
    if str(i) in nodes:
        n = nodes[str(i)]
        print(f"  {i:3d} {n['id']:30s} {n['title']}")

print("\nSchmidt's Dramatic Situations (55 situations, lines 21-75):")
for i in range(21, 76, 5):
    if str(i) in nodes:
        n = nodes[str(i)]
        print(f"  {i:3d} {n['id']:30s} {n['title']}")

print("\nPropp's Functions (31 functions, lines 76-106):")
for i in range(76, 107, 5):
    if str(i) in nodes:
        n = nodes[str(i)]
        print(f"  {i:3d} {n['id']:30s} {n['title']}")

print("\nVogler's Hero's Journey (12 stages, lines 107-118):")
for i in range(107, 119):
    if str(i) in nodes:
        n = nodes[str(i)]
        print(f"  {i:3d} {n['id']:30s} {n['title']}")

print("\nCampbell's Hero's Journey (17 stages, lines 119-135):")
for i in range(119, 136):
    if str(i) in nodes:
        n = nodes[str(i)]
        print(f"  {i:3d} {n['id']:30s} {n['title']}")

# Now build the manual mapping
print("\n\n=== MANUAL TROPE KEYING ===\n")
print("Review each trope and assign its best matching node...\n")

# Pre-built mapping based on semantic analysis
manual_mapping = {
    "SecretPetPlot": ("10", "high"),  # Temptation - hiding something against rules
    "SecretRelationship": ("14", "high"),  # Love/romance
    "SecretTest": ("112", "high"),  # Tests - secret trial
    "SecretTestOfCharacter": ("112", "high"),  # Tests/challenges to character
    "SecretlyDying": (None, "low"),  # No clear node - internal condition
    "SeekingTheIntangible": ("1", "medium"),  # Quest variant
    "SeekingUltimateStrength": ("1", "medium"),  # Quest for something
    "SelectiveEnforcement": (None, "low"),  # Meta-trope about rules
    "SendInTheSearchTeam": ("84", "high"),  # Mediation - search party dispatched
    "SeparatedAtBirth": ("41", "medium"),  # Enigma/discovery
    "SequelHook": (None, "low"),  # Meta/ending trope
    "SequencingDeception": (None, "low"),  # Narrative technique, not plot instance
    "SerendipityShock": ("14", "medium"),  # Unexpected fortune in love/relationships
    "SerialKiller": ("51", "high"),  # Madness/killer menacing
    "SeriesFauxnale": (None, "low"),  # Meta-trope about structure
    "SeriesGoal": (None, "low"),  # Meta-objective, not plot move
    "SetRightWhatOnceWentWrong": ("17", "medium"),  # Discovery/quest to fix past
    "SettlingTheFrontier": ("2", "medium"),  # Adventure/journey
    "SexAsRiteOfPassage": ("13", "medium"),  # Maturation/coming of age
    "SexEqualsLove": ("14", "high"),  # Love plot
    "SexForServices": ("43", "medium"),  # Obtaining through exchange
    "SexyManInstantHarem": ("8", "low"),  # Rivalry for his attention?
    "ShaggyDogStory": (None, "low"),  # Meta about structure
    "ShaveAndAHaircut": (None, "low"),  # Audio/stylistic, not plot
    "SheCleansUpNicely": ("12", "low"),  # Transformation in appearance
    "SheIsNotMyGirlfriend": ("14", "medium"),  # Love/romance denial
    "ShipTease": ("14", "high"),  # Love plot moments
    "ShipwreckStart": ("5", "medium"),  # Escape/survival from wreck
    "ShockAndSwitchEnding": (None, "low"),  # Ending twist, not plot instance
    "ShootTheShaggyDog": ("20", "high"),  # Descension - death negates efforts
    "ShowWithinAShow": (None, "low"),  # Format/structure trope
    "ShutUpHannibal": ("58", "medium"),  # Conviction - hero challenges villain's ideology
    "ShutUpKiss": ("14", "high"),  # Love/romance
    "SidekickGlassCeiling": (None, "low"),  # Meta-limitation
    "SigningOffCatchPhrase": (None, "low"),  # Format trope
    "SinkOrSwimFatherhood": ("13", "medium"),  # Maturation/responsibility
    "SinkingShipScenario": ("114", "high"),  # Ordeal/crisis
    "SkippingSchool": ("10", "medium"),  # Temptation/violation
    "SlapSlapKiss": ("14", "high"),  # Love/romance with conflict
    "SleepCute": ("14", "low"),  # Love moment
    "SleepLearning": ("112", "low"),  # Test variant
    "SlowAndSteadyWinsTheRace": ("47", "high"),  # Competition/race
    "SlumberPartyPloy": ("10", "high"),  # Temptation/violation of rules
    "SmallMindedVillain": ("20", "medium"),  # Descension - petty villain
    "SnicketWarningLabel": (None, "low"),  # Meta/format
    "SnipeHunt": ("79", "high"),  # Trickery - deceiving with false quest
    "SnowballingThreat": ("84", "medium"),  # Mediation/urgent threat grows
    "SnowedIn": ("5", "high"),  # Escape/confinement
    "SoNearYetSoFar": ("113", "high"),  # Approach to inmost cave
    "SoOnceAgainTheDayIsSaved": (None, "low"),  # Meta/narration trope
    "SoWhatDoWeDoNow": (None, "low"),  # Existential question post-adventure
    "SolemnEndingTheme": (None, "low"),  # Audio/format
    "SomeoneToRememberHimBy": ("71", "high"),  # Loss - loved one dies leaving legacy
    "SomethingWeForgot": (None, "low"),  # Structural/pacing
    "SorcerersApprenticePlot": ("87", "medium"),  # First function of donor - apprenticeship
    "SouvenirLand": (None, "low"),  # Meta/location trope
    "SpeakNowOrForeverHoldYourPeace": ("108", "high"),  # Call to adventure/climax
    "SpeedDating": ("14", "low"),  # Love/romance search
    "SpellingBee": ("47", "low"),  # Competition
    "SplitAndReunion": ("40", "medium"),  # Reunion of split selves
    "SplitTimelinesPlot": (None, "low"),  # Narrative structure
    "SpotTheImpostor": ("99", "high"),  # Unrecognized arrival variant
    "StalkerShot": (None, "low"),  # Camera/visual technique
    "StandardHeroReward": ("106", "high"),  # Wedding/reward
    "StartMyOwn": ("35", "medium"),  # Revolt - dissatisfaction leads to action
    "StartOfDarkness": ("20", "high"),  # Descension begins - villain origin
    "StartToCorpse": ("83", "high"),  # Villainy - body discovered
    "StarterVillain": ("68", "medium"),  # Starter villain opposition
    "StarterVillainStays": ("68", "medium"),  # Continuing opposition
    "StartsWithASuicide": ("51", "high"),  # Madness/despair
    "StartsWithTheirFuneral": ("71", "high"),  # Loss - death event
    "StepOneEscape": ("5", "high"),  # Escape from confinement
    "SternChase": ("96", "high"),  # Pursuit/chase
    "StockClockHandHang": (None, "low"),  # Visual/stunt trope
    "StockEvilOverlordTactics": ("83", "high"),  # Villainy plans
    "StockSeriesFinales": (None, "low"),  # Meta structure
    "StockSitcomGrandFinale": (None, "low"),  # Meta structure
    "StoneSoup": ("79", "high"),  # Trickery
    "StopTheHeroTwist": (None, "low"),  # Ending twist structure
    "StormInATeacup": (None, "low"),  # Scale/stakes trope
    "StormingTheCastle": ("116", "high"),  # Road back - final assault
    "StorybookEpisode": (None, "low"),  # Format/genre trope
    "StorybookOpening": (None, "low"),  # Format/style
    "StrangerBehindTheMask": ("99", "high"),  # Unrecognized arrival
    "StrangerInAFamiliarLand": ("118", "medium"),  # Return with elixir - home changed
    "StrangerInAStrangeSchool": ("74", "high"),  # Fish out of water
    "StrangersOnATrainPlotMurder": ("35", "high"),  # Conspiracy/agreement
    "StuffBlowingUp": ("116", "medium"),  # Climactic action
    "StumbledIntoThePlot": ("84", "high"),  # Mediation - hero stumbles into quest
    "StumblingUponTheLostWizard": ("87", "high"),  # First function - finding helper
    "StylisticCallback": (None, "low"),  # Meta/reference trope
    "Suburbia": (None, "low"),  # Setting, not plot instance
    "SubvertedSuspicionAesop": (None, "low"),  # Lesson/twist
    "SuccessionCrisis": ("35", "high"),  # Revolt/succession struggle
    "SuddenDownerEnding": ("20", "high"),  # Descension ending
    "SuddenIntelligence": ("12", "low"),  # Transformation variant
    "SuddenMusicalEnding": (None, "low"),  # Format trope
    "SugarApocalypse": ("31", "high"),  # Disaster strikes
    "SuicidalCosmicTemperTantrum": ("51", "medium"),  # Madness/cosmic force
    "SuicideMission": ("59", "high"),  # Self-sacrifice quest
    "SummonEverymanHero": ("84", "high"),  # Mediation - hero summoned
    "SuperPowersForADay": ("89", "medium"),  # Provision of agent (magical)
    "SuperheroEpisode": (None, "low"),  # Meta/format
    "SuperheroOrigin": ("107", "medium"),  # Ordinary world becomes special
    "SuperweaponSurprise": (None, "low"),  # Twist/revelation
    "SupportingCharactersSayGoodbye": ("118", "medium"),  # Return with elixir - homecoming
    "SurpriseParty": ("22", "low"),  # Benefaction variant
    "SurprisinglyHappyEnding": ("19", "high"),  # Ascension ending
    "SurprisinglyMundaneReason": (None, "low"),  # Revelation/twist
    "SurvivalThroughSelfSacrifice": ("59", "high"),  # Self-sacrifice paradox
    "SurvivedTheBeginning": (None, "low"),  # Survival/armor trope
    "SuspicionAesop": (None, "low"),  # Lesson structure
    "SuspiciouslySpecificSermon": (None, "low"),  # Dialogue/thematic
    "SwearWordPlot": (None, "low"),  # Behavior/language trope
    "SymbolicHeroRebirth": ("117", "high"),  # Resurrection/rebirth
    "SympatheticWithAddedContext": ("41", "medium"),  # Enigma/revelation
    "SystematicVillainTakedown": ("83", "high"),  # Villainy defeated systematically
    "TagAlongActor": ("87", "low"),  # Journey with mentor variant
    "TagTeamSuicide": ("51", "high"),  # Madness/miscommunication death
    "TakeAThirdOption": (None, "low"),  # Choice/twist structure
    "TakeCareOfTheKids": ("56", "high"),  # Sacrifice for loved ones
    "TakeMyHand": ("116", "medium"),  # Road back - rescue moment
    "TakeOverTheCity": ("35", "high"),  # Revolt/takeover
    "TakeOverTheWorld": ("35", "high"),  # Revolt/conquest goal
    "TakeUpMySword": ("84", "high"),  # Mediation - hero accepts task
    "TakeYourChildToWorkDayPlot": (None, "low"),  # Domestic trope
    "TakenDuringTheEnding": (None, "low"),  # Ending structure
    "TakingOverHeaven": ("35", "high"),  # Revolt against supreme authority
    "TakingOverTheTown": ("35", "high"),  # Revolt/takeover
    "TalentContest": ("47", "high"),  # Competition
    "TalkShowAppearance": (None, "low"),  # Format trope
    "TalkingYourWayOut": ("79", "high"),  # Trickery with words
    "TallTale": (None, "low"),  # Story/legend trope
    "TeachHimAnger": ("52", "low"),  # Genius/growth variant
    "TeacherStudentRomance": ("15", "high"),  # Forbidden love (age/power taboo)
    "TechnicianVersusPerformer": ("27", "low"),  # Competition/rivalry
    "TenLittleMurderVictims": ("37", "high"),  # Daring enterprise/mystery
    "ThatDidntHappen": (None, "low"),  # Denial/revision
    "ThatOneSummer": (None, "low"),  # Memory/setting
    "ThatsAllFolks": (None, "low"),  # Format/closing
    "TheBGrade": (None, "low"),  # Achievement anxiety
    "TheBadGuyWins": ("20", "high"),  # Descension/villain victory
    "TheBardOnBoard": (None, "low"),  # Reference/adaptation
    "TheBet": ("27", "high"),  # Competition/wager
    "TheBigBadShuffle": (None, "low"),  # Villain swap twist
    "TheBigDamnKiss": ("14", "high"),  # Love/romance climax
    "TheBigRace": ("47", "high"),  # Competition/race
    "TheBreakfastPlot": ("73", "high"),  # Odd couple - mismatched group bonds
    "TheBrideWithAPast": (None, "low"),  # Secret revelation
    "TheCakeIsALie": ("34", "high"),  # Becoming fortunate reversed - trick
    "TheCallHasBadReception": ("108", "low"),  # Call variant
    "TheCallKnowsWhereYouLive": ("108", "high"),  # Call to adventure compelled
    "TheCallLeftAMessage": ("108", "high"),  # Call to adventure
    "TheCallPutMeOnHold": ("108", "medium"),  # Call variant - extraordinary person
    "TheCaper": ("37", "high"),  # Daring enterprise/heist
    "TheCaptivityNarrative": ("39", "high"),  # Abduction/captivity
    "TheCavalry": ("32", "high"),  # Miracle/rescue arrives
    "TheCavalryArrivesLate": ("116", "high"),  # Road back - rescue too late
    "TheChainOfHarm": ("6", "medium"),  # Revenge/cycle of abuse
    "TheChase": ("3", "high"),  # Pursuit
    "TheChooserOfTheOne": ("109", "medium"),  # Refusal/selection variant
    "TheCollector": ("27", "high"),  # Competition for collection
    "TheCon": ("79", "high"),  # Trickery/scam
    "TheConspiracy": ("35", "high"),  # Conspiracy/plot uncovered
    "TheConvenientStoreNextDoor": (None, "low"),  # Logistics detail
    "TheDayOfReckoning": ("114", "high"),  # Ordeal/final confrontation
    "TheDogBitesBack": ("6", "high"),  # Revenge/payback
    "TheDragonsComeBack": ("2", "medium"),  # Adventure - dragons return
    "TheDulcineaEffect": ("14", "medium"),  # Love at first sight
    "TheEnd": (None, "low"),  # Format/closing
    "TheEndOfTheBeginning": ("107", "high"),  # Ordinary world changes
    "TheEndOrIsIt": (None, "low"),  # Ambiguous ending
    "TheEndingChangesEverything": (None, "low"),  # Twist ending
    "TheEvilsOfFreeWill": ("35", "high"),  # Tyranny/control ideology
    "TheFellowshipHasEnded": ("118", "medium"),  # Return - group separates
    "TheFinalTemptation": ("10", "high"),  # Temptation before victory
    "TheFunInFuneral": (None, "low"),  # Tone/style trope
    "TheGameNeverStopped": ("112", "medium"),  # Test deception
    "TheGamePlaysYou": ("10", "high"),  # Temptation/danger disguised
    "TheGlomp": ("14", "low"),  # Love/affection moment
    "TheGoodGuysAlwaysWin": ("19", "high"),  # Ascension/victory
    "TheGoodKingdom": ("107", "high"),  # Ordinary world - peaceful setting
    "TheGreatRepair": ("37", "high"),  # Daring enterprise/repair quest
    "TheGreatestStoryNeverTold": ("118", "low"),  # Unrecognized return/achievement
    "TheGrovel": ("14", "high"),  # Love/romance reconciliation
    "TheHero": ("107", "high"),  # Ordinary world hero
    "TheHeroDies": ("20", "high"),  # Descension/death ending
    "TheHollywoodFormula": (None, "low"),  # Meta structure
    "TheHomewardJourney": ("116", "high"),  # Road back - journey home
    "TheIdolsBlessing": ("87", "high"),  # Donor - idol grants boon
    "TheInfiltration": ("79", "high"),  # Trickery/infiltration
    "TheInspectorIsComing": ("112", "medium"),  # Test/inspection
    "TheJungleOpera": ("2", "medium"),  # Adventure in wild territory
    "TheMagicComesBack": ("32", "high"),  # Miracle - magic returns
    "TheMagicGoesAway": ("31", "high"),  # Disaster - magic vanishes
    "TheMagnificentSevenSamurai": ("37", "high"),  # Daring enterprise/assembly
    "TheMakeover": ("12", "high"),  # Transformation/change appearance
    "TheManBehindTheCurtain": ("198", "high"),  # Expose - villain revealed
    "TheMasochismTango": ("14", "low"),  # Toxic love dynamic
    "TheMigration": ("2", "medium"),  # Adventure/journey to new home
    "TheMovingExperience": ("2", "medium"),  # Separation/journey
    "TheOneWhoMadeItOut": ("19", "high"),  # Ascension from poverty
    "TheOnlyOne": ("108", "high"),  # Call - only hero can solve
    "ThePictureCameWithTheFrame": (None, "low"),  # Object/twist
    "ThePromPlot": (None, "low"),  # Event/social structure
    "ThePromisedLand": ("108", "high"),  # Call/goal - promised destination
    "TheQueenWillBeWatching": ("112", "medium"),  # Test with observer
    "TheQuest": ("1", "high"),  # Quest plot
    "TheResolutionWillNotBeIdentified": (None, "low"),  # Format/meta
    "TheReveal": (None, "low"),  # Revelation/twist structure
}

# Build results list
results = []
for i, trope in enumerate(tropes, 1):
    slug = trope["slug"]
    if slug in manual_mapping:
        node_id, conf = manual_mapping[slug]
    else:
        print(f"WARNING: {slug} not in manual mapping, checking...")
        node_id, conf = None, "low"

    results.append({
        "slug": slug,
        "node": node_id,
        "alt": None,
        "conf": conf
    })

# Write JSON
output_path = r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\keys.batch7.json"
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

# Validation
keyed_count = sum(1 for r in results if r["node"] is not None)
null_count = len(results) - keyed_count

print(f"\nResults written to {output_path}")
print(f"Total tropes keyed: {keyed_count}")
print(f"Null nodes: {null_count}")

# Validate IDs
valid_ids = set(nodes.keys())
errors = 0
for r in results:
    if r["node"] and r["node"] not in valid_ids:
        print(f"ERROR: Invalid node {r['node']} for {r['slug']}")
        errors += 1

if errors == 0:
    print(f"✓ All {keyed_count} node IDs valid!")
