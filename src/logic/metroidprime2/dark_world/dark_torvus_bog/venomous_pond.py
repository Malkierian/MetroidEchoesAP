from BaseClasses import MultiWorld

from ... import (
    can_use_light_beam,
    can_use_screw_attack,
    has_dark_suit,
    has_light_suit,
    can_activate_safe_zone,
    can_use_grapple_beam,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or


class VenomousPond_BroodingGroundSide(MetroidPrime2Region):
    name = "Venomous Pond"
    desc = "Brooding Ground Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Crystal Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (High Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                state.has("Morph Ball", player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Brooding Ground (Venomous Pond Side)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_and([
                # consider the amount of energy tank to return to safety
                condition_or([
                    condition_and([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            state.count("Energy Tank", player) >= 1,
                            has_dark_suit(state, player),
                        ]),
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]


class VenomousPond_CrystalPlatform(MetroidPrime2Region):
    name = "Venomous Pond"
    desc = "Crystal Platform"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Temple Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Portal Chamber Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Brooding Ground Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                can_use_light_beam(state, player),
            ]),
        ),
    ]


class VenomousPond_HighSafeZone(MetroidPrime2Region):
    name = "Venomous Pond"
    desc = "High Safe Zone"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Brooding Ground Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    state.has("Space Jump Boots", player),
                    state.has("Morph Ball", player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Crystal Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Item)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    can_use_grapple_beam(state, player),
                ]),
            ]),
        ),
    ]


class VenomousPond_Item(MetroidPrime2Region):
    name = "Venomous Pond"
    desc = "Item"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Brooding Ground Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Crystal Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (High Safe Zone)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    can_use_grapple_beam(state, player),
                ]),
            ]),
        ),
    ]

    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Pickup (Dark Torvus Key 3)",
            can_access=lambda state, player: True,
        )


class VenomousPond_PortalChamberSide(MetroidPrime2Region):
    name = "Venomous Pond"
    desc = "Portal Chamber Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Portal Chamber (Venomous Pond Side)",
            door=DoorCover.Dark,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Crystal Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
    ]


class VenomousPond_SaveStationSide(MetroidPrime2Region):
    name = "Venomous Pond"
    desc = "Save Station Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Brooding Ground Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                can_use_screw_attack(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Temple Access Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_and([
                    can_activate_safe_zone(state, player),
                    condition_or([
                        state.count("Energy Tank", player) >= 1,
                        has_dark_suit(state, player),
                    ]),
                ]),
                has_light_suit(state, player),
            ]),
        ),
    ]


class VenomousPond_TempleAccessSide(MetroidPrime2Region):
    name = "Venomous Pond"
    desc = "Temple Access Side"
    exits_ = [
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Dark Torvus Temple Access (Venomous Pond Side)",
            door=DoorCover.Light,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Crystal Platform)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_or([
                # consider the amount of energy tank to return to safety
                condition_or([
                    condition_and([
                        can_activate_safe_zone(state, player),
                        condition_or([
                            state.count("Energy Tank", player) >= 1,
                            has_dark_suit(state, player),
                        ]),
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Dark Torvus Bog - Venomous Pond (Save Station Side)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                condition_or([
                    # consider the amount of energy tank to return to safety
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player),
                ]),
                state.has("Space Jump Boots", player),
            ]),
        ),
    ]
