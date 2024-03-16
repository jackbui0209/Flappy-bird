import pygame, random

def initialize_colors():
	GREEN = (0, 200, 0)
	BLUE = (0, 102, 255)
	PINK = (255, 0, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	return GREEN, BLUE, PINK, BLACK, RED

def initialize_tubes_parameters(DISPLAY_WIDTH, DISPLAY_HEIGHT):
	TUBE_WIDTH = DISPLAY_WIDTH / 6 
	OX_TUBE_SPACE = DISPLAY_WIDTH / 4
	OY_TUBE_SPACE = DISPLAY_HEIGHT / 4
	TUBE_VELOCITY = 3
	x_tube1 =  (4 * DISPLAY_WIDTH) / 6
	x_tube2 = x_tube1 + TUBE_WIDTH +  OX_TUBE_SPACE
	x_tube3 = x_tube2 + TUBE_WIDTH +  OX_TUBE_SPACE
	tube1_height = random.randint(100, 500)
	tube2_height = random.randint(100, 500)
	tube3_height = random.randint(100, 500)
	tube1_passed = False
	tube2_passed = False
	tube3_passed = False
	return TUBE_WIDTH, OX_TUBE_SPACE, OY_TUBE_SPACE, TUBE_VELOCITY, x_tube1, x_tube2, x_tube3, tube1_height, tube2_height, tube3_height, tube1_passed, tube2_passed, tube3_passed

def initialize_bird_parameters(DISPLAY_WIDTH, DISPLAY_HEIGHT):
	BIRD_ACCELERATION = 0.4
	BIRD_SIZE = DISPLAY_WIDTH / 20
	bird_velocity = 0
	x_bird = ( 2 * DISPLAY_WIDTH) / 15
	y_bird = (30 * DISPLAY_HEIGHT) / 80
	return BIRD_ACCELERATION, BIRD_SIZE, bird_velocity, x_bird, y_bird

def initialize_fonts():
	font = pygame.font.SysFont("sans",20)
	font1 = pygame.font.SysFont("sans",70)
	font2 = pygame.font.SysFont("sans",40)
	return font, font1, font2

def set_image(WIDTH, HEIGHT, file_name):
	image = pygame.image.load(file_name)
	image = pygame.transform.scale(image, (WIDTH, HEIGHT))
	return image

def initialize_audio_files():
	fly_audio = pygame.mixer.Sound("audio_wing.wav")
	point_audio = pygame.mixer.Sound("audio_point.wav")
	hit_audio = pygame.mixer.Sound("audio_hit.wav")
	die_audio = pygame.mixer.Sound("audio_die.wav")
	return fly_audio, point_audio, hit_audio, die_audio

def initialize_necessary_parameters():
	running = True
	score = 0 
	is_game_over = False
	return running, score, is_game_over

def started_process(screen, clock, GREEN, background_image):
		clock.tick(60)
		screen.fill(GREEN)
		screen.blit(background_image, (0,0))

def initialize_tubes_object_process(screen, tubes_color, TUBE_WIDTH, OX_TUBE_SPACE, OY_TUBE_SPACE, TUBE_VELOCITY, x_tube1, x_tube2, x_tube3, tube1_height, tube2_height, tube3_height, tube1_passed, tube2_passed, tube3_passed, DISPLAY_WIDTH, DISPLAY_HEIGHT):
		tube1 = pygame.draw.rect(screen, tubes_color, (x_tube1, 0, TUBE_WIDTH, tube1_height))
		tube2 = pygame.draw.rect(screen, tubes_color, (x_tube2, 0, TUBE_WIDTH, tube2_height))
		tube3 = pygame.draw.rect(screen, tubes_color, (x_tube3, 0, TUBE_WIDTH, tube3_height))
		tube1_inver = pygame.draw.rect(screen, tubes_color, (x_tube1, tube1_height + OY_TUBE_SPACE, TUBE_WIDTH, DISPLAY_HEIGHT - tube1_height - OY_TUBE_SPACE))
		tube2_inver = pygame.draw.rect(screen, tubes_color, (x_tube2, tube2_height + OY_TUBE_SPACE, TUBE_WIDTH, DISPLAY_HEIGHT - tube2_height - OY_TUBE_SPACE))
		tube3_inver = pygame.draw.rect(screen, tubes_color, (x_tube3, tube3_height + OY_TUBE_SPACE, TUBE_WIDTH, DISPLAY_HEIGHT - tube3_height - OY_TUBE_SPACE))
		x_tube1 -= TUBE_VELOCITY
		x_tube2 -= TUBE_VELOCITY
		x_tube3 -= TUBE_VELOCITY
		return tube1, tube2, tube3, x_tube1, x_tube2, x_tube3, tube1_inver, tube2_inver, tube3_inver

def initialize_infinity_tubes(DISPLAY_WIDTH, OX_TUBE_SPACE, TUBE_WIDTH):
	x_tube = DISPLAY_WIDTH + OX_TUBE_SPACE - TUBE_WIDTH
	tube_height = random.randint(100, 500)
	tube_passed = False	
	return x_tube, tube_height, tube_passed

def initialize_bird_object_process(screen, bird_image, x_bird, y_bird, bird_velocity, BIRD_ACCELERATION):
	bird = screen.blit(bird_image, (x_bird, y_bird))
	bird_velocity += BIRD_ACCELERATION
	y_bird += bird_velocity
	return bird, bird_velocity, y_bird 

def score_ponits_process():
		pygame.mixer.Sound.play(point_audio)
		score += 1
		tube_passed = True
		return 
def main():
	pygame.init()
	pygame.display.set_caption('Flappy Bird')
	DISPLAY_WIDTH = 600
	DISPLAY_HEIGHT = 800
	screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
	clock = pygame.time.Clock()
	GREEN, BLUE, PINK, BLACK, RED = initialize_colors()
	TUBE_WIDTH, OX_TUBE_SPACE, OY_TUBE_SPACE, TUBE_VELOCITY, x_tube1, x_tube2, x_tube3, tube1_height, tube2_height, tube3_height, tube1_passed, tube2_passed, tube3_passed = initialize_tubes_parameters(DISPLAY_WIDTH, DISPLAY_HEIGHT)
	BIRD_ACCELERATION, BIRD_SIZE, bird_velocity, x_bird, y_bird = initialize_bird_parameters(DISPLAY_WIDTH, DISPLAY_HEIGHT)
	font, font1, font2 = initialize_fonts()
	background_image = set_image(DISPLAY_WIDTH, DISPLAY_HEIGHT + 20, "background.png" )
	bird_image = set_image(BIRD_SIZE, BIRD_SIZE, "bird.png" )
	fly_audio, point_audio, hit_audio, die_audio = initialize_audio_files()
	running, score, is_game_over = initialize_necessary_parameters()

	while running:		
		started_process(screen, clock, GREEN, background_image)
		tube1, tube2, tube3, x_tube1, x_tube2, x_tube3, tube1_inver, tube2_inver, tube3_inver = initialize_tubes_object_process(screen, BLUE, TUBE_WIDTH, OX_TUBE_SPACE, OY_TUBE_SPACE, TUBE_VELOCITY, x_tube1, x_tube2, x_tube3, tube1_height, tube2_height, tube3_height, tube1_passed, tube2_passed, tube3_passed, DISPLAY_WIDTH, DISPLAY_HEIGHT)
		if x_tube1 < -TUBE_WIDTH:
			x_tube1, tube1_height, tube1_passed = initialize_infinity_tubes(DISPLAY_WIDTH, OX_TUBE_SPACE, TUBE_WIDTH) 
		if x_tube2 < -TUBE_WIDTH:
			x_tube2, tube2_height, tube2_passed = initialize_infinity_tubes(DISPLAY_WIDTH, OX_TUBE_SPACE, TUBE_WIDTH) 
		if x_tube3 < -TUBE_WIDTH:
			x_tube3, tube3_height, tube3_passed = initialize_infinity_tubes(DISPLAY_WIDTH, OX_TUBE_SPACE, TUBE_WIDTH) 
		bird, bird_velocity, y_bird = initialize_bird_object_process(screen, bird_image, x_bird, y_bird, bird_velocity, BIRD_ACCELERATION)

		if (x_tube1 + TUBE_WIDTH) < x_bird and tube1_passed == False:
			pygame.mixer.Sound.play(point_audio)
			score += 1
			tube1_passed = True
		if (x_tube2 + TUBE_WIDTH) < x_bird and tube2_passed == False:
			pygame.mixer.Sound.play(point_audio)
			score += 1
			tube2_passed = True
		if (x_tube3 + TUBE_WIDTH) < x_bird and tube3_passed == False:
			pygame.mixer.Sound.play(point_audio)
			score += 1
			tube3_passed = True

		score_text = font.render("Score: " + str(score), True, BLACK)
		screen.blit(score_text, (10,10))
		for tube in [tube1, tube2, tube3, tube1_inver, tube2_inver, tube3_inver]:
			if bird.colliderect(tube) or y_bird > 750 :
				TUBE_VELOCITY = 0
				bird_velocity = 0
				BIRD_ACCELERATION = 0
				game_over_text = font1.render("GAME OVER", True, RED)
				screen.blit(game_over_text, (150,300))
				game_over_text2 = font2.render("SCORE: " + str(score), True, RED)
				screen.blit(game_over_text2, (240,380))
				game_over_text3 = font.render("Press SPACE to replay", True, RED)
				screen.blit(game_over_text3, (230, 440))		
				is_game_over = True

		mouse_x, mouse_y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if (0 < mouse_x < 600) and (0 < mouse_y < 800):
						bird_velocity = 0
						y_bird -= 80
						pygame.mixer.Sound.play(fly_audio)
					if is_game_over:
						x_tube1 = 400
						x_tube2 = 650
						x_tube3 = 900
						y_bird = 300					
						TUBE_VELOCITY = 3
						bird_velocity = 0
						BIRD_ACCELERATION = 0.4
						score = 0
						tube1_height = random.randint(100, 500)
						tube2_height = random.randint(100, 500)
						tube3_height = random.randint(100, 500)						
						is_game_over = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bird_velocity = 0
					y_bird -= 80
					pygame.mixer.Sound.play(fly_audio)
					if is_game_over:
						x_tube1 = 400
						x_tube2 = 650
						x_tube3 = 900
						y_bird = 300					
						TUBE_VELOCITY = 3
						bird_velocity = 0
						BIRD_ACCELERATION = 0.4
						score = 0
						tube1_height = random.randint(100, 500)
						tube2_height = random.randint(100, 500)
						tube3_height = random.randint(100, 500)
						is_game_over = False
		pygame.display.flip()
	pygame.quit()
main()