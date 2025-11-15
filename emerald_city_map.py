"""
Emerald City Map - A Turtle Graphics Adventure
==============================================
Navigate the yellow brick road through a pixel-art Emerald City
and find the Wizard (a badly drawn green rectangle)!

Copyright notice: This is an original work inspired by the public domain
elements of L. Frank Baum's "The Wonderful Wizard of Oz" (1900).
"""

import turtle
import random
import time
import math


class EmeraldCity:
    """Main class for the Emerald City map generator."""
    
    def __init__(self):
        """Initialise the Emerald City with turtle graphics."""
        self.screen = turtle.Screen()
        self.screen.setup(width=1200, height=900)
        self.screen.bgcolor("#0d3321")  # Darker emerald green for contrast
        self.screen.title("🏰 Emerald City Map - Find the Wizard! 🏰")
        self.screen.tracer(0)  # Turn off auto-update for better performance
        
        # Create the drunk Roomba turtle for the yellow brick road
        self.roomba = turtle.Turtle()
        self.roomba.shape("circle")
        self.roomba.color("#f4d03f")  # Yellow
        self.roomba.shapesize(1.5, 1.5)
        self.roomba.pensize(20)
        self.roomba.speed(0)
        
        # Create a turtle for drawing buildings
        self.builder = turtle.Turtle()
        self.builder.hideturtle()
        self.builder.speed(0)
        
        # Create a turtle for glitter effects
        self.glitter = turtle.Turtle()
        self.glitter.hideturtle()
        self.glitter.speed(0)
        
        # Track if wizard is found
        self.wizard_found = False
        self.wizard_position = None
        self.collectibles = []
        self.score = 0
        self.emerald_count = 0
        
        # Create score display
        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.color("#ffd700")
        self.score_display.speed(0)
        
    def draw_pixel_building(self, x, y, width, height, colour, is_wizard=False):
        """
        Draw a pixel-art style building.
        
        Args:
            x: X coordinate
            y: Y coordinate
            width: Building width
            height: Building height
            colour: Building colour
            is_wizard: Whether this is the Wizard's building
        """
        self.builder.penup()
        self.builder.goto(x, y)
        self.builder.pendown()
        self.builder.fillcolor(colour)
        self.builder.begin_fill()
        
        # Draw main building rectangle
        for _ in range(2):
            self.builder.forward(width)
            self.builder.left(90)
            self.builder.forward(height)
            self.builder.left(90)
        
        self.builder.end_fill()
        
        if is_wizard:
            # Mark the wizard's building with animated stars
            self.builder.penup()
            self.builder.goto(x + width/2, y + height + 10)
            self.builder.color("#ffff00")  # Bright yellow for visibility
            self.builder.write("★ WIZARD ★", align="center", 
                             font=("Impact", 16, "bold"))
            
            # Draw a magical aura around wizard's building
            self.builder.penup()
            self.builder.goto(x - 10, y - 10)
            self.builder.pendown()
            self.builder.color("#00ff00")
            self.builder.pensize(3)
            for _ in range(4):
                self.builder.forward(width + 20)
                self.builder.left(90)
            self.builder.pensize(1)
            self.builder.color(colour)
            self.wizard_position = (x + width/2, y + height/2)
        else:
            # Add windows to regular buildings
            self.draw_windows(x, y, width, height)
    
    def draw_windows(self, x, y, width, height):
        """Draw pixel-art windows on a building."""
        window_colour = "#ffeb3b"  # Bright yellow for lit windows
        window_size = min(width, height) // 8
        
        rows = max(2, height // (window_size * 3))
        cols = max(2, width // (window_size * 3))
        
        for row in range(rows):
            for col in range(cols):
                if random.random() > 0.3:  # 70% chance of lit window
                    wx = x + (col + 1) * (width / (cols + 1)) - window_size/2
                    wy = y + (row + 1) * (height / (rows + 1)) - window_size/2
                    
                    self.builder.penup()
                    self.builder.goto(wx, wy)
                    self.builder.pendown()
                    self.builder.fillcolor(window_colour)
                    self.builder.begin_fill()
                    
                    for _ in range(4):
                        self.builder.forward(window_size)
                        self.builder.left(90)
                    
                    self.builder.end_fill()
    
    def create_city(self):
        """Generate the Emerald City with random pixel-art buildings."""
        building_colours = [
            "#27ae60",  # Emerald green
            "#2ecc71",  # Light green
            "#16a085",  # Sea green
            "#1abc9c",  # Turquoise
            "#3498db",  # Blue
            "#9b59b6",  # Purple
        ]
        
        # Create a grid of buildings with more variety
        buildings = []
        for i in range(-4, 5):
            for j in range(-3, 3):  # Removed top row (changed from -3,4 to -3,3)
                x = i * 130
                y = j * 130
                # Make top row buildings shorter to not block title
                if j == 2:
                    width = random.randint(40, 70)
                    height = random.randint(50, 80)
                else:
                    width = random.randint(50, 90)
                    height = random.randint(70, 130)
                colour = random.choice(building_colours)
                buildings.append((x, y, width, height, colour))
        
        # Pick one building to be the Wizard's (make it badly drawn)
        wizard_idx = random.randint(0, len(buildings) - 1)
        
        for idx, (x, y, width, height, colour) in enumerate(buildings):
            if idx == wizard_idx:
                # Wizard's building - badly drawn green rectangle
                self.draw_pixel_building(x, y, width, height, "#00ff00", is_wizard=True)
            else:
                self.draw_pixel_building(x, y, width, height, colour)
        
        # Add floating emeralds to collect
        self.create_emeralds()
        
        self.screen.update()
    
    def create_emeralds(self):
        """Create collectible emeralds scattered around the city."""
        emerald_turtle = turtle.Turtle()
        emerald_turtle.hideturtle()
        emerald_turtle.speed(0)
        
        for _ in range(12):
            x = random.randint(-500, 500)
            y = random.randint(-350, 350)
            self.collectibles.append((x, y))
            
            # Draw emerald gem
            emerald_turtle.penup()
            emerald_turtle.goto(x, y)
            emerald_turtle.color("#50c878")
            emerald_turtle.begin_fill()
            for _ in range(6):
                emerald_turtle.forward(10)
                emerald_turtle.left(60)
            emerald_turtle.end_fill()
            
            # Add sparkle
            emerald_turtle.goto(x, y + 5)
            emerald_turtle.color("#ffffff")
            emerald_turtle.dot(3)
    
    def glitter_explosion(self, x, y, intensity="normal"):
        """Create a glitter explosion effect at the given position."""
        colours = ["#ffd700", "#ffeb3b", "#fff59d", "#ffffff", "#e1bee7", "#ce93d8", "#50c878"]
        
        num_particles = random.randint(12, 20) if intensity == "mega" else random.randint(8, 15)
        
        for _ in range(num_particles):
            self.glitter.penup()
            self.glitter.goto(x, y)
            self.glitter.color(random.choice(colours))
            self.glitter.pendown()
            
            # Random direction and length
            angle = random.randint(0, 360)
            length = random.randint(25, 70) if intensity == "mega" else random.randint(20, 60)
            self.glitter.setheading(angle)
            
            # Draw sparkle line with more variation
            for i in range(length):
                self.glitter.forward(1)
                if random.random() > 0.65:
                    self.glitter.penup()
                    if random.random() > 0.8:
                        self.glitter.dot(3)
                else:
                    self.glitter.pendown()
        
        try:
            self.screen.update()
        except:
            pass
    
    def update_score_display(self):
        """Update the score display on screen."""
        try:
            self.score_display.clear()
            self.score_display.goto(-580, 420)
            self.score_display.color("#00ff00")  # Bright green for visibility
            self.score_display.write(f"💎 Emeralds: {self.emerald_count}/12 | Score: {self.score}", 
                                    align="left", font=("Arial", 15, "bold"))
        except:
            pass  # Screen may be closing
    
    def check_emerald_collection(self):
        """Check if Roomba has collected any emeralds."""
        rx, ry = self.roomba.xcor(), self.roomba.ycor()
        
        for emerald_pos in self.collectibles[:]:
            ex, ey = emerald_pos
            distance = math.sqrt((rx - ex)**2 + (ry - ey)**2)
            
            if distance < 25:
                # Collect emerald!
                self.collectibles.remove(emerald_pos)
                self.emerald_count += 1
                self.score += 100
                
                # Clear the emerald with a small explosion
                self.glitter_explosion(ex, ey, intensity="normal")
                
                # Play "sound" with visual feedback
                self.play_sound_effect("collect")
                self.update_score_display()
                
                # Check if all emeralds collected
                if self.emerald_count == 12:
                    self.score += 500
                    self.update_score_display()
                    self.play_sound_effect("bonus")
    
    def play_sound_effect(self, effect_type):
        """Simulate sound effects with visual feedback."""
        try:
            # Reuse existing glitter turtle instead of creating new ones
            if effect_type == "collect":
                self.glitter.penup()
                self.glitter.goto(self.roomba.xcor(), self.roomba.ycor() + 20)
                self.glitter.color("#50c878")
                self.glitter.write("♪ Ding! +100", align="center", font=("Arial", 10, "bold"))
            elif effect_type == "bonus":
                self.glitter.penup()
                self.glitter.goto(0, 0)
                self.glitter.color("#ffd700")
                self.glitter.write("★ BONUS! +500 ★", align="center", font=("Arial", 16, "bold"))
        except:
            pass
    
    def drunk_roomba_path(self, steps=100):
        """
        Draw the yellow brick road with a wandering drunk Roomba algorithm.
        
        Args:
            steps: Number of steps the Roomba takes
        """
        self.roomba.penup()
        # Start from bottom left
        self.roomba.goto(-500, -350)
        self.roomba.pendown()
        self.roomba.color("#f4d03f")  # Yellow brick road colour
        
        self.update_score_display()
        
        last_turn = 0
        trail_colour = "#f4d03f"
        
        for step in range(steps):
            try:
                # Drunk Roomba behaviour: mostly forward with random turns
                if random.random() > 0.68:  # 32% chance to turn
                    turn_angle = random.choice([-50, -35, -20, -10, 10, 20, 35, 50])
                    self.roomba.left(turn_angle)
                    last_turn = step
                    
                    # Glitter explosion on turns/corners!
                    self.score += 10
                    self.glitter_explosion(self.roomba.xcor(), self.roomba.ycor(), intensity="normal")
                    self.update_score_display()
                
                # Gradually change trail colour for rainbow effect
                if step % 5 == 0:
                    colours = ["gold", "orange", "yellow", "gold"]
                    trail_colour = random.choice(colours)
                    self.roomba.color(trail_colour)
                
                # Move forward a random distance
                distance = random.randint(18, 38)
                self.roomba.forward(distance)
            except:
                # Window was closed
                return
            
            # Check for emerald collection
            self.check_emerald_collection()
            
            # Check if we're near the wizard
            if self.wizard_position:
                wx, wy = self.wizard_position
                rx, ry = self.roomba.xcor(), self.roomba.ycor()
                distance_to_wizard = math.sqrt((wx - rx)**2 + (wy - ry)**2)
                
                if distance_to_wizard < 60 and not self.wizard_found:
                    self.wizard_found = True
                    bonus = 1000 if self.emerald_count == 12 else 500
                    self.score += bonus
                    self.celebrate_victory()
            
            # Bounce off edges with mega explosion
            if abs(self.roomba.xcor()) > 580 or abs(self.roomba.ycor()) > 430:
                self.roomba.left(180 + random.randint(-35, 35))
                self.score += 25
                self.glitter_explosion(self.roomba.xcor(), self.roomba.ycor(), intensity="mega")
                self.update_score_display()
            
            # Update display periodically
            if step % 3 == 0:
                try:
                    self.screen.update()
                    time.sleep(0.04)
                except:
                    break  # Screen closed
        
        self.screen.update()
    
    def celebrate_victory(self):
        """Celebrate finding the Wizard with a big glitter explosion!"""
        if self.wizard_position is None:
            return
        
        wx, wy = self.wizard_position
        
        # Massive glitter explosion extravaganza!
        for i in range(8):
            self.glitter_explosion(wx, wy, intensity="mega")
            if i % 2 == 0:
                # Create expanding ring effect
                self.create_ring_effect(wx, wy, radius=50 + i * 20)
        
        # Victory message
        self.glitter.penup()
        self.glitter.goto(0, -380)
        self.glitter.color("#00ff00")  # Wicked green!
        self.glitter.write("🎉 YOU FOUND THE WIZARD! 🎉", 
                          align="center", 
                          font=("Impact", 26, "bold"))
        
        # Show final score
        self.glitter.goto(0, -415)
        self.glitter.color("#ffff00")  # Bright yellow
        all_emeralds = " - PERFECT! ALL EMERALDS!" if self.emerald_count == 12 else ""
        self.glitter.write(f"Final Score: {self.score}{all_emeralds}", 
                          align="center", 
                          font=("Arial", 18, "bold"))
        self.screen.update()
    
    def create_ring_effect(self, x, y, radius):
        """Create an expanding ring effect for celebrations."""
        ring = turtle.Turtle()
        ring.hideturtle()
        ring.speed(0)
        ring.penup()
        ring.goto(x, y - radius)
        ring.pendown()
        ring.color("#ffd700")
        ring.pensize(3)
        ring.circle(radius)
        try:
            self.screen.update()
        except:
            pass
    
    def add_instructions(self):
        """Add game instructions to the screen."""
        instruction_turtle = turtle.Turtle()
        instruction_turtle.hideturtle()
        instruction_turtle.penup()
        instruction_turtle.goto(0, 420)
        instruction_turtle.color("#00ff00")  # Bright green for readability
        instruction_turtle.write("🏰 EMERALD CITY MAP 🏰", 
                                align="center", 
                                font=("Courier New", 28, "bold"))
        
        instruction_turtle.goto(0, 390)
        instruction_turtle.color("#ffff00")  # Bright yellow for contrast
        instruction_turtle.write("Follow the yellow brick road to find the Wizard!", 
                                align="center", 
                                font=("Arial", 14, "bold"))
        
        instruction_turtle.goto(0, 368)
        instruction_turtle.color("#00ff88")  # Bright cyan-green
        instruction_turtle.write("💎 Collect all 12 emeralds for a perfect score!", 
                                align="center", 
                                font=("Arial", 13, "bold"))
        
        instruction_turtle.goto(0, -440)
        instruction_turtle.color("#ff69ff")  # Bright magenta
        instruction_turtle.write("✨ Watch for glitter explosions at corners! ✨", 
                                align="center", 
                                font=("Arial", 13, "bold italic"))
    
    def run(self):
        """Run the complete Emerald City map experience."""
        print("*** Welcome to Emerald City! ***")
        print("Building the city...")
        
        self.add_instructions()
        self.create_city()
        
        print("Following the yellow brick road...")
        print("Watch for glitter explosions when the turtle hits corners!")
        print("Collect emeralds for bonus points!")
        print("")
        
        self.drunk_roomba_path(steps=180)
        
        if not self.wizard_found:
            # Give a hint if wizard wasn't found
            self.glitter.penup()
            self.glitter.goto(0, -380)
            self.glitter.color("#ff3333")  # Bright red for visibility
            self.glitter.write("The Wizard is hiding in the building marked with ★", 
                              align="center", 
                              font=("Arial", 15, "bold"))
            self.glitter.goto(0, -415)
            self.glitter.color("#ffff00")  # Yellow for score
            self.glitter.write(f"Final Score: {self.score} | Emeralds: {self.emerald_count}/12", 
                              align="center", 
                              font=("Arial", 16, "bold"))
            self.screen.update()
        
        print(f"\n*** Quest complete! Final Score: {self.score} ***")
        print(f"Emeralds Collected: {self.emerald_count}/12")
        print("Click the window to exit.")
        self.screen.exitonclick()


def main():
    """Main entry point for the Emerald City map."""
    city = EmeraldCity()
    city.run()


if __name__ == "__main__":
    main()
