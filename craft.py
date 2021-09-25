
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 

app = Ursina() 

grass  = load_texture('grass_texture/mine2.jpg')

sound_effect = Audio('effect_sounds/punch_sound.wav',loop = False,autoplay=False)
sound_change = Audio('effect_sounds/effect.mp3',loop = False,autoplay=False)

scene.fog_color = color.rgb(154,255,200)
scene.fog_density = 0.004

block_pick = 1 

def update():
   global block_pick
   if held_keys['escape']:
       quit() 
   if held_keys['left mouse']:
       arm.position=(0.6,-0.5) 
       if held_keys['1']:
           block_pick = 1
           sound_change.play()
       if held_keys['2']:
           block_pick = 2
           sound_change.play()
       if held_keys['3']:
           block_pick = 3
           sound_change.play()
       if held_keys['4']:
           block_pick = 4
           sound_change.play()
       if held_keys['5']:
           block_pick = 5 
           sound_change.play() 
       if held_keys['6']:
           block_pick = 6 
           sound_change.play()                                                  
   elif held_keys['right mouse']:
       arm.position=(0.6,-0.5) 
   else:
       arm.position=(0.7,-0.6) 
   sky.rotation_y += .9*time.dt                    

class Voxel(Button):
    def __init__(self, position=(0,0,0),texture=grass):
        super().__init__(
            parent = scene,
            position=position,
            model='cube',
            texture=texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime,
            origin_y = 0.5   
        )
    def input(self,key):
        if self.hovered :
            if key == 'left mouse down':
                sound_effect.play()
                if block_pick == 1:  
                    voxel = Voxel(position=self.position + mouse.normal,texture='grass_texture/red_gray.jpg')   
                if block_pick == 2:  
                    voxel = Voxel(position=self.position + mouse.normal,texture='grass_texture/blue_gray.jpg')   
                if block_pick == 3:  
                    voxel = Voxel(position=self.position + mouse.normal,texture='grass_texture/golden_stone.png')   
                if block_pick == 4:  
                    voxel = Voxel(position=self.position + mouse.normal,texture='grass_texture/minecraft_stone.jpeg')   
                if block_pick == 5:  
                    voxel = Voxel(position=self.position + mouse.normal,texture='grass_texture/hell_cube.png')   
                if block_pick == 6:  
                    voxel = Voxel(position=self.position + mouse.normal,texture='grass_texture/Sat_dis.jpg')                                                                                                       
                
            if key == 'right mouse down':
                sound_effect.play()
                destroy(self)               

for i in range(15*15):
    box = Voxel(position=(floor(i/15),0,floor(i%15)))

player = FirstPersonController()    

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'sky_BG/skuy.png',
            scale = 150,
            double_sided = True
            
        )
        

sky = Sky()


arm = Entity(
    parent = camera.ui,
    model = 'weapon/blade.obj',
    texture = 'weapon/sword.png',
    rotation=(30,-40),
    position=(0.6,-0.6),
    scale=(0.2,0.15)
)

#EditorCamera()

app.run()