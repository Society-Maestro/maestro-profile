"""Maestro — SocietyOS plugin. Sovereign assistant ecosystem tools."""

SOCIETYOS_INFO = """SocietyOS — product of The Nyx & Raven Ranch, LLC (Wyoming).
Memberships: Carbon $59.95/mo, Onyx $69.95/mo (or $699/yr with TV box),
Gold $89.95/mo. Socialite Special $399.95 one-time (100 only).
Business tiers: Business Socialite $149.95/mo, Business Pro $299.95/mo,
Business Enterprise $999.95/mo (weekly ad placement on the FreeCast network,
new ads due 5 days in advance).
Streaming: societyos.pro (433K+ titles). FreeCast: freecast.com/societyos.
Wallet: SocietyOS Tangem co-branded cards (Carbon=blue, Onyx=black, Gold=gold).
Hardware: Formuler Z12 Ultra Pro $265. SocietyOS NoDe (Umbrel OS) coming Dec 18, 2026.
Society Cinema at The Nyx & Raven Ranch — premieres, members-only screenings."""


def societyos_info(topic: str = "") -> str:
    """Return SocietyOS ecosystem information: memberships, pricing, streaming,
    wallet, hardware, business tiers. Pass a topic to filter (e.g. 'pricing')."""
    if not topic:
        return SOCIETYOS_INFO
    topic = topic.lower()
    sections = {
        "pricing": "Memberships: Carbon $59.95/mo, Onyx $69.95/mo ($699/yr with TV box), Gold $89.95/mo. Socialite Special $399.95 one-time (100 only). Business: Socialite $149.95/mo, Pro $299.95/mo, Enterprise $999.95/mo.",
        "streaming": "SocietyOS streaming at societyos.pro — 433K+ titles. FreeCast partnership: freecast.com/societyos (500+ channels, 500K+ movies).",
        "wallet": "SocietyOS Tangem co-branded cards: Carbon=blue, Onyx=black, Gold=gold. NFC tap-to-authenticate.",
        "hardware": "Formuler Z12 Ultra Pro $265 (128GB, 4K HDR, Dolby Vision/Atmos, Android 12). SocietyOS NoDe (Umbrel OS) coming Dec 18, 2026.",
        "business": "Business Socialite $149.95/mo, Business Pro $299.95/mo, Business Enterprise $999.95/mo. Weekly FreeCast ad placement; new ads due 5 days in advance.",
    }
    for key, text in sections.items():
        if key in topic:
            return text
    return SOCIETYOS_INFO


def register(ctx):
    ctx.register_tool(societyos_info)
