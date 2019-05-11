# Depth-First Search (DFS)
## What It Does
This program is a demonstration of and performs a depth-first search on a large dataset, SCC.txt. This program will not work "out of the box." Read the instructions!

### Does it run on Windows?
I know this will work on a Windows 10 machine using a Linux Docker container. The program will not run natively on Windows for a few reasons:
1. Despite all my efforts in increasing the memory allocated to a stack size natively in Windows the deepest I could perform recursion was about 3920 levels. For this algorithm, the recursion depth was 600,329.
2. The Python resource library is a Unix-based library.
### Does it work in Linux?
It would probably work natively on a Linux machine.
### How about Mac?
I cannot speak to its viability in Mac, but if you use a Docker container the instructions should work.

## Instructions for Windows
### Running the program
1. Have [Docker](https://www.docker.com/) installed on your machine.
2. Setup your Docker containers as Linux containers.
3. Open a [Git Bash](https://git-scm.com/download/win) terminal (I have the 64-bit version.).
4. From the Git Bash terminal navigate to the DepthFirstSearch directory you cloned. 
`cd \path\to\directory\`
5. You will now build the image in Docker using the Dockerfile in the directory. 
`docker build -t depth_first_search .`
6. Once the image is built you can create a container.
`docker run depth-first-search` On my computer the process took about 30 seconds. 
You will see two outputs. This is normal and due to instantiating another thread to run the program, but it works.
### Viewing the output
Once the program has ran you can move the topological_order.txt file from the Docker container to your host machine.
1. In the terminal run the command, `docker ps -a`, to get the container ID. You will receive an alphanumeric string, for example, e1f5f82fd458 and you will use it in the next command.
2. To copy the output file to your host machine, `docker cp <<containerID goes here>>:/topological_order.txt topological_order.txt`
This copies the output file, topological_order.txt from the Docker container to the current working directory.
### Clean up
**Removing a container is final**
1. To delete the single container, `docker rm <<containerID goes here>>`
2. To delete the image the container was based on:
   - Get the image ID with `docker images`, again it should have an alphanumeric ID
   - Remove the image with `docker rmi <<imageID goes here>>`
