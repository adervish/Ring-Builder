
import maya.cmds as cmds

initials = [
[0,0,0],
[0,0,2],
[0,1,0],
[1,2,2],
[0,0,0],
[0,2,1]
];

def nurbs_ring():
	print "Hello world"
	
	ring_diameter = 19
	ring_height = 3
	ring_thickness = 1
	divit_diameter = 1.5
	divit_depth = .5
	
	cmds.nurbsSquare( d=2, nr=(1, 0, 0), c=(0, 0, ring_diameter/2 + ring_thickness), sl1=ring_thickness, sl2=ring_height, name='ring',  constructionHistory=0 )
	cmds.revolve( 'topring', ax=(0, 1, 0), p=(0, 0, 0) )
	cmds.revolve( 'bottomring', ax=(0, 1, 0), p=(0, 0, 0) )
	cmds.revolve( 'rightring', ax=(0, 1, 0), p=(0, 0, 0) )
	cmds.revolve( 'leftring', ax=(0, 1, 0), p=(0, 0, 0) )
	
	cmds.nurbsSquare( d=2, nr=(1, 0, 0), c=(0, 0, 0), sl2=divit_diameter/2, sl1=divit_depth, name='bit',  constructionHistory=0 )
	cmds.revolve( 'topbit', ax=(0, 0, 1), p=(0, 0, 0) )
	cmds.revolve( 'bottombit', ax=(0, 0, 1), p=(0, 0, 0) )
	cmds.revolve( 'rightbit', ax=(0, 0, 1), p=(0, 0, 0) )
	cmds.revolve( 'leftbit', ax=(0, 0, 1), p=(0, 0, 0) )
	
#	cmds.cylinder( r=divit_diameter/2, axis=(0, 0, 1), pivot=(0, 0, 1), heightRatio=divit_depth/divit_diameter/2)
	
#	cmds.circle(radius = ring_diameter/2, nr=[0,1,0], name='ring')
#	cmds.circle(radius = ring_diameter/2 - ring_thickness, nr=[0,1,0], name='ring_inner')#


def a_ring():
	
	ring_diameter = 22 # outer diameter 
	ring_thickness = 1.5
	divit_diameter = 1.5
	divit_depth = .75
	ring_height = 4
	#divit_spacing = .5

	divits = []
	cmds.polyPipe(radius=ring_diameter/2, height=ring_height*2, thickness=ring_thickness, name='ring0')
	cmds.setAttr( 'polyPipe1.subdivisionsAxis', 20 )
	
	for x in range(0,6):
		for y in range(0,3):	
			letter = initials[x]
			symbol = letter[y]
			myName = "_c" + str(x) + str(y)
			
			if symbol == 0 :
				cmds.polyCylinder(axis=[0,0,1], radius=(divit_diameter/2), height=divit_depth, name=myName)
			elif symbol == 2:
				cmds.polyCylinder(axis=[0,0,1], radius=(divit_diameter/2), height=ring_thickness * 2.1, name=myName)
		
			if symbol != 1:
				divits.append(myName)	
				y_off = 0
				cmds.move(0,y_off,(ring_diameter/2 - divit_depth/2 + .3),myName)
				cmds.rotate(0,(x*3+y)*20,0,myName, pivot=[0,0,0])
		
	rn = 0;	
	for d in divits[:]:
		print 'ring' + str(rn) + " " + d
		cmds.polyBoolOp('ring' + str(rn), d, op=2, n='ring' + str(rn+1), )
		rn += 1


def r_ring():
	
	ring_diameter = 20 # outer diameter 
	ring_thickness = 1.5
	divit_diameter = 1.5
	divit_depth = .75
	ring_height = 8.5
	divit_spacing = .75

	divits = []
	cmds.polyPipe(radius=ring_diameter/2, height=ring_height*2, thickness=ring_thickness, name='ring0')
	cmds.setAttr( 'polyPipe1.subdivisionsAxis', 360 )
	
	for x in range(0,6):
		for y in range(0,3):	
			letter = initials[x]
			symbol = letter[y]
			myName = "_c" + str(x) + str(y)
			
			if symbol == 0 :
				cmds.polyCylinder(axis=[0,0,1], radius=(divit_diameter/2), height=divit_depth, name=myName)
			elif symbol == 2:
				cmds.polyCylinder(axis=[0,0,1], radius=(divit_diameter/2), height=ring_thickness * 2.1, name=myName)
		
			if symbol != 1:
				divits.append(myName)	
				y_off = (y - 1) * (divit_diameter + divit_spacing)
				cmds.move(0,y_off,(ring_diameter/2 - divit_depth/2 + .2),myName)
				cmds.rotate(0,(13*(x)),0,myName, pivot=[0,0,0])
		
	rn = 0;	
	for d in divits[:]:
		print 'ring' + str(rn) + " " + d
		cmds.polyBoolOp('ring' + str(rn), d, op=2, n='ring' + str(rn+1), )
		rn += 1
			
			
			