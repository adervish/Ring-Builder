
initials = [
[0,0,0],   
[0,0,2],  
[0,1,0], 
[1,2,2],  
[0,0,0],   
[0,2,1]   
];

d_width=1.5;
d_w_width=1.75;

r_height = 3;
r_diameter = 19; 
r_thickness = 1.25;

res = 20;

$fn = res;

module divit_0(i)
{
  rotate([90,0,i*20]) 
  translate([0,0,r_diameter/2 + r_thickness/2])	
  cylinder(h=r_thickness/2, r=d_width/2);
}

module divit_1(i)
{
}

module divit_2(i)
{
  rotate([90,0,i*20]) 
  translate([0,0,r_diameter/2-r_thickness*.10])	
  cylinder(h=r_thickness*1.10, r1=d_w_width/2,r2=d_width/2);
}

module r2d()
{
  union() {
  translate([r_thickness/2,r_height/2,0]) scale([1/10,1/10,1]) circle(r=r_thickness/2*10);
  translate([r_thickness/2,-1*r_height/2,0]) scale([1/10,1/10,1]) circle(r=r_thickness/2*10);
  translate([r_thickness/2,0,0]) square(size=[r_thickness,r_height], center=true);


  }
}

module ring()
{   
  difference() {
	rotate_extrude(convexity=10, $fn=res*6) translate([r_diameter/2,0,0])  r2d();
    echo("here");
    for(i = [0:17] )
    {
        b = i % 3;
        a = floor(i / 3);
        echo(b, a);
        
        symbol = initials[a][b];
        if( symbol == 0 )
        {
            divit_0(i);
        }
        else if ( symbol == 1 )
        {
            divit_1(i);
        }
        else if (symbol == 2) 
        {
            divit_2(i);
        }

    }
  }

}

module main()
{
   ring();
}

main();