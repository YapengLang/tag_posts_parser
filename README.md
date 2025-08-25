# tag_posts_parser

This is a parser to parse students posts of Theoritical Application Genetics in ANU-Shandong University joint colleage. This project powered by [private Piazza api](https://github.com/hfaran/piazza-api).

**Install**

In terminal

```bash
cd <YOUR_PATH>
git clone https://github.com/YapengLang/tag_posts_parser.git
cd <YOUR_PATH>/tag_posts_parser
pip install .
```

*Need python >=3.11 and <3.14. Creating a new conda env is recommanded.

Check codes integrity [optional]

```bash
pip install pytest
pytest
```

we expect all tests passed 🟢🟢🟢🟢🟢

**Use**

In terminal, run
```bash
python -m tpp
```

You will be asked several questions
```bash
Email: <TYPE YOUR ANSWER>
Password: <TYPE YOUR ANSWER>
Your course's Piazza network ID: <FIND IN YOUR COURSE DOMAIN> 
```
The first two you should type in your credentials for logging in the Piazza system. The last one you can find on your course page, see an e.g. in highlight:
<img width="838" height="223" alt="image" src="https://github.com/user-attachments/assets/df6418fa-bc63-4d81-910e-199bca1663db" />

If all work, you will need to customise the deadline for each learning module (aka folder, as in Piazza):
```bash
Please provide deadline for each folder in format 2025-8-10-17, or press Enter to skip:
Deadline for folder introlecture: <TYPE YOUR TIME OR ENTER>
Deadline for folder cq-lm5: <TYPE YOUR TIME OR ENTER>
...
```

*IMPORTANT:* the deadline you provide should be in format YYYY-MM-DD-HH. HH is in 24 hr. 2025-08-09-17 is the same as 2025-8-9-17. If you press enter instead of typing deadline, we will skip the statistic for that learning module (folder).

Finally, define the output folder:

```bash
What is the folder you want to write the summary csv to? <TYPE YOUR OUT FOLDER PATH>
```

I just try ~/Desktop/. Should be good!
Then you will get your output in ~/Desktop/summary.csv 

Yay!


**License**  
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).  
Commercial use of this code or its derivatives is **not permitted**.
