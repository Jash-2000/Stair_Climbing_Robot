# Articulated Arm for parcel delivery

This folder contains the scripts to control a mobile manipulator to pick up a block ( the luggage our bot is carrying), carry it to a new configuration, and place it at the door step. To achieve this, our software will plan a multi-segment trajectory( Arm + Base Station) for the end-effector of the mobile manipulator; implement a feedback controller to drive the wheels and arm joints of the mobile manipulator; and simulate the mobile manipulator's motion given the wheel and joint velocities calculated by the controller. 

![384px-Youbot-capstone](https://user-images.githubusercontent.com/47540320/121959719-c46f4080-cd82-11eb-9675-0405a696dff2.png)


This simulator developed, will use odometry to simulate the motion of the chassis. To animate the bot, add config.csv to hbox in V-REP GUI. To generate the csv file, we need to run main.py. Some of the details and limitations are as follows:

1. There is a speed limit check for velocity of both wheels and joints in simulate.py. The parameter to set the limit can be found in bot_params.yaml.

2. testJointLimits is also implemented in feedback_controller.py to ensure that the joints after timestep and the given joint speeds do not violate the joint limits. For this the violating joint limits are noted and their corresponding column in the Je matrix is set to zero so as to ensure that the constraint joint do not contribute further to achieve the desired configuration.

3. In order to avoid singularity, the pseudo jacobian inverse is given a tolerance of 1e-3

4. Also provision to change the time scaling and trajectory type is also added in parameters in config folder

---

## Other Details

Please find the following files/folders along with this file:
  * Code Folder
    1. config
      * Bot_params.yaml
      ```
          Contains configuration of the bot like chassis and arm dimensions, joint limits, joint and wheel velocity limits and initial configuration of the bot
      ```
      * Trajectory_params.yaml
      ```
        Contains configuration of cube wrt space frame and trajectory information like type of trajectory (Screw or Cartesian), max linear and angular velocity which
        determines number of configuration between two end effector configuration and tuning parameters.
      ```
    2. simulate.py
    ```
      Python file which computes odometry
    ```
    3. trajectory.py
    ```
      Python file which computes the trajectory of end effector wrt space frame
    ```
    4. feedback_controller.py
    ```
      Python file which computes required joint and wheel velocity to achieve the desired configuration from a given current configuration.
    ```
    5. main.py
    ```
      Python file to execute to generate required results (config.csv and plot.png)
    ```
  * Results Folder
    1. readme.txt
    ```
      Contains information regarding cube configurations and tuning parameter
    ```
    2. config.csv
    ```
    Csv file to be inputted to the vrep simulator to animate the bot
    ```
    3. animation.mp4
    ```
      Animation video of execution.
    ```
    4. error.csv
    ```
       CSV file having Xerr data along with time
    ```
    5. plot and log images
    ```
      Images showing Xerr with time
    ```

---

## Output GIF

![vlc-record-2021-06-15-04h02m21s-animation mp4-](https://user-images.githubusercontent.com/47540320/121967831-b1fb0400-cd8e-11eb-821b-ce423cb9e27d.gif)

For V-REP installation guide, visit its [official page.](http://hades.mech.northwestern.edu/index.php/Getting_Started_with_the_CoppeliaSim_Simulator)
