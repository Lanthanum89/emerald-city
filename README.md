# 🏰 Emerald City Map 🏰

A whimsical turtle graphics adventure where you follow a wandering yellow brick road through a pixel-art Emerald City to find the Wizard!

![Emerald City Map Screenshot](https://github.com/user-attachments/assets/emerald-city-screenshot.png)

*The drunk Roomba turtle creates a wandering yellow brick road through the pixel-art city, with glitter explosions at every turn!*

## Features

✨ **Pixel-Art Buildings**: 63 randomly generated emerald-themed buildings with animated lit windows  
🛤️ **Yellow Brick Road**: Watch as a turtle draws a wandering path like a drunk Roomba with rainbow trail effects  
💫 **Enhanced Glitter Explosions**: Spectacular sparkly effects with varying intensity (normal & mega) whenever the turtle turns or hits edges  
🎯 **Mini-Quest**: Find the Wizard, represented as a badly drawn green rectangle with a magical golden aura  
💎 **Collectible Emeralds**: Gather all 12 scattered emeralds for bonus points and a perfect score  
📊 **Scoring System**: Earn points for turns (+10), edge bounces (+25), emerald collection (+100), and finding the Wizard (+500/+1000)  
🎨 **Visual Effects**: Expanding ring celebrations, simulated sound effects with visual feedback, and animated score display  
🎉 **Victory Celebration**: Massive glitter extravaganza with multiple explosions when you find the Wizard  

## Installation

Requires Python 3.6+ with the `turtle` module (included in standard Python installations).

```bash
python emerald_city_map.py
```

## How It Works

1. The programme generates a pixel-art Emerald City with 63 randomly placed buildings
2. 12 collectible emerald gems are scattered throughout the city
3. One building is chosen to be the Wizard's hideout (marked with ★ and a green aura)
4. A turtle draws the yellow brick road using an enhanced "drunk Roomba" algorithm that:
   - Mostly moves forward with variable speed
   - Randomly turns at unpredictable moments (32% chance)
   - Creates glitter explosions with varying intensity
   - Bounces off the edges with mega explosions
   - Automatically collects emeralds when passing nearby
   - Changes trail colour for a subtle rainbow effect
5. The scoring system rewards exploration:
   - +10 points for each turn
   - +25 points for edge bounces  
   - +100 points for each emerald collected
   - +500 bonus for all 12 emeralds
   - +500/+1000 for finding the Wizard
6. When the turtle gets close to the Wizard's building, you win with an epic celebration!

## Controls

- Simply watch the animation unfold
- Click the window when finished to exit

## Copyright Notice

This is an original work inspired by the public domain elements of L. Frank Baum's *The Wonderful Wizard of Oz* (1900). All code and creative implementations are original.

## Customisation

You can modify the following in the code:

- `steps` parameter in `drunk_roomba_path()` - controls how long the road is (currently 180)
- Building colours in the `building_colours` list (6 different emerald shades)
- Window frequency (currently 70% chance of lit windows)
- Glitter explosion intensity, colours, and particle count
- Roomba turning probability (currently 32%)
- Number of collectible emeralds (currently 12)
- Scoring values for different actions
- Trail colour variations for rainbow effects
- Screen size and background colour

## Screenshot

The screenshot above shows:

- **Bright green title** at the top in wicked gothic-style font
- **Yellow instruction text** telling you to follow the yellow brick road
- **Cyan emerald collection prompt** for bonus points
- **Magenta glitter message** at the bottom
- **Score display** in the top-left showing emeralds collected (1/12) and current score (830)
- **Pixel-art buildings** in emerald greens, blues, and purples with lit yellow windows
- **Emerald gems** (hexagonal green shapes) scattered around the city
- **Yellow brick road** with rainbow colour variations (gold, orange, yellow) creating a drunk Roomba path
- **Glitter explosions** with white sparkle particles at turns and corners
- **The Wizard's building** marked with "★ WIZARD ★" in bright yellow with a green outline
- **Bottom message** showing the Wizard wasn't found and final score
- **Readable text** with high contrast colours (bright yellows, greens, and magentas against dark emerald background)

## Example Output

The programme creates:

- A darker emerald green background for better contrast (1200x900 window)
- 54 randomly positioned pixel-art buildings with animated windows (top row removed for title visibility)
- One special bright green building marked with "★ WIZARD ★" in Impact font with a golden aura
- 12 hexagonal emerald gems scattered throughout the city
- A meandering yellow brick road with rainbow colour variations (gold, orange, yellow)
- Real-time score tracking in the top-left corner with bright green text
- Spectacular glitter effects at turns and edges (normal & mega intensity)
- Visual "sound effects" for collecting emeralds and bonuses
- Epic victory celebration with expanding rings and massive explosions when the Wizard is found
- Final score display showing total points and emeralds collected in readable fonts

## Technical Details

- Uses Python's `turtle` graphics module
- Object-oriented design with the `EmeraldCity` class
- Optimised rendering with `screen.tracer(0)` for better performance
- Random seed ensures a different city layout each time

Follow the yellow brick road and may your journey be filled with glitter

---
