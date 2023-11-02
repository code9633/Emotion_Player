class EmojiSelector:
    def __init__(self, label):
        self.label = label
    
    def selectEmoji(self):
        emojis = {
            0 : {
                "emoji" : '/images/Emoji/Angry.png',
                "quotes" : "Where there is anger,there is always pain underneath"
                
            },
            
            1 : {
                "emoji" : '/images/Emoji/Happy.png',
                "quotes" : "Happiness is a function of accepting what is"
                
            },
            
            2:{
                "emoji" : '/images/Emoji/Sad.png',
                "quotes" : "The only way to get things from the past is by looking at them"
                
            },
            3:{
                "emoji" : '/images/Emoji/Neutral.png',
                "quotes" : "See the good in all things"
            }   
        }
        
        return emojis[int(self.label)]