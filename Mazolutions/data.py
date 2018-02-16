from Mazolutions.models import Mazolution, MazolutionStep

mazs = Mazolution.objects.all()

p = Mazolution() 
s = MazolutionStep()

if len(mazs) > 0:
    p = mazs[0]
else:
    p = Mazolution(problem_title="search selected text in google",author="linzhu", solution_overview="search selected text in google")
    p.save()

if len(p.steps.all()) > 0:
    s = p.steps.all()[0]
else:
    s = MazolutionStep(mazolution=p,number=1,name="get clipboard as @keyword", 
        automation="""
         const {clipboard} = require('electron');
          this.engineContext.result = clipboard.readText();
          """)
    s.save()
    

