# awsi - find AWS instance ids and log stream names exactly when needed

awsi is a small python script that integrates into the linux command line.

![Just a gif...](./awsi.gif)


If you find yourself typing a command like

```aws ec2 get-console-output --instance-id```

and realize, that you have no idea, what the instance id of the service in question is, awsi comes in handy.

Just type ```Alt+i``` and browse throug a descriptive representation of all your instances (even stopped ones, if they are still available) using fzf.
If you select one, its instance id is pasted directly into your cursor position, completing your command.


The same works with ```Alt+g``` for log groups, useful e.g. for ```awslogs```.


## Installation
```git clone git@github.com:jochen-oko/awsi.git```
```cd awsi```
```./install.sh``` (remember to source your rc-file for instant integration...)



Supported shells are currently zsh and bash. If you can provide the functionality for other shells, just send me a pull request. The setup for the shortcuts is inside ```install.sh```
