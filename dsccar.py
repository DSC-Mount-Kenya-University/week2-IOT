Motor motor0(0x4010581C6148);
Network network1(0xDFE19B16);

while(true)
{
	if (	motor0.setAngle(0,0);
	motor1.setAngle(0,0);
)

	
	while(network0.getJoystickDirection()==JOYSTICK_UP)
	{
		motor1.setSpeed(100,-100);
		motor0.setSpeed(-100,100);
	}
	while(network0.getJoystickDirection()==JOYSTICK_DOWN)
	{
		motor1.setSpeed(-100,100);
		motor0.setSpeed(100,-100);
	}
	while(network0.getJoystickDirection()==JOYSTICK_LEFT)
	{
		motor0.setSpeed(-25,-50);
		motor1.setSpeed(50,25);
	}
	while(network0.getJoystickDirection()==JOYSTICK_RIGHT)
	{
		motor1.setSpeed(-25,-50);
		motor0.setSpeed(50,25);
	}
}
