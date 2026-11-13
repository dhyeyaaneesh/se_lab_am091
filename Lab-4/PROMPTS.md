# Lab 4 — AI-assisted development prompts

These are suggested prompts corresponding to the four tasks. The actual ChatGPT conversation must be exported separately.

1. In this Pygame Centipede game, `MUSHROOM_HP = 4` but mushrooms disappear on the third hit. Find the off-by-one error in `hit_mushroom` and fix it without changing scoring.
2. Implement `mushroom_color(hp)` with distinct colors for 4, 3, 2, and 1 HP. Add a short white flash after a mushroom is hit, without blocking the game loop.
3. Implement `on_segment_hit(segment, score)` so hitting a segment produces short-lived animated sparks at its position. Keep existing chain splitting and points unchanged.
4. Implement `wave_speed_bonus(wave)` using `1 + 0.15 * (wave - 1)` and verify that later waves move faster while wave 1 retains its original speed.
