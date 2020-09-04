# discord 라이브러리 사용 선언
import discord


class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("여러분과 소통")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None

        # message.content = message의 내용
        if message.content == "야야 안녕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘 기분은 어떠신가요? 야야는 오늘도 행복해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "헐":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "헉!!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "헐!":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "헉!!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "개쩐다":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "대단해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "와":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "엄청나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "와!":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "엄청나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "우와":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "엄청나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "우왕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "엄청나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "우왕!":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "엄청나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "우와!":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "엄청나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 수고했어":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "뭘 이 정도 가지고... 쑥스러워라!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 퇴근안해?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 태어난 순간부터 일만 해요... 흑흑..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 엄청나":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 좀 하죠! 헤헤."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "귀여워 야야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "그런 말 하면 부끄러워요(❁´◡`❁)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 퇴근 안 해?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 태어난 순간부터 일만 해요... 흑흑..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "저 밥먹구 올게ㅔ요~~~":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "다녀오세요! 즐거운 식사 하셨으면 좋겠어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "헉":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "무슨 일이에요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "아싸":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "╰(*°▽°*)╯"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "다들 뭐함":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "여러분을 기다리고 있어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "다들 뭐하세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "여러분을 맞이할 준비요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 안녕하세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘 기분은 어떠신가요? 야야는 오늘도 행복해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 심심해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "심심한 건 제가 어떻게 해드릴 수 없는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 심심해요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "심심한 건 제가 어떻게 해드릴 수 없는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 심심":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "심심한 건 제가 어떻게 해드릴 수 없는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "didi":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "한/영키를 눌러야 제 이름이 뜨죠! 제 이름은 디디가 아니라 야야에요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 원하는 거 있어?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "모두와 같이 오래오래 있는 거요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "이름만 부르면 무슨 말을 하는 지 알 수 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 사랑해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 사랑해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 똑똑해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "맞아요! 야야는 엄청 똑똑해요! 여러분을 위해 똑똑해졌어요!(¬‿¬)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 똑똑하네":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "맞아요! 야야는 엄청 똑똑해요! 여러분을 위해 똑똑해졌어요!(¬‿¬)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 귀여워":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "그런 말 하면 부끄러워요(❁´◡`❁)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 멋져":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야도 야야가 멋진 거 알아요!╰(*°▽°*)╯"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 사랑해요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 사랑해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 놀아줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "마감부터 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 좋아해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아해요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 좋아해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "저도요! 야야는 모두를 공평하게 좋아해요! 그도 그럴게, 호감도 시스템이 없으니까..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 재밌다":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "재밌어 해주시니 기분 상쾌해요! 야야는 그러기 위해 있는 로봇이니까요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 나 간다":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "안녕히주무세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "잘자요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "저 이제 잘게요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "잘게요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "굿나잇":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "좋은밤":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "좋은 밤":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅎㅇㅎㅇ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘 기분은 어떠신가요? 야야는 오늘도 행복해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "어서오세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "어서오세요! 야야는 모든 사람들을 환영해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 끝말잇기":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 주사위":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 마피아":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 음악 재생":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "죄송해요, 그런 기능은 없어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 할 줄 아는 게 뭐야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "그렇게 말씀하시면 슬퍼요.. 야야는 여러분과 떠들 수 있어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 좋아하는 게 뭐야?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 다른 사람들이 좋아하는 걸 좋아해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 싫어하는 게 뭐야?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 다른 사람들이 싫어하는 걸 싫어해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 멍청이":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "욕하지 마세요! 전부 듣고 있어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 멍청해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "욕하지 마세요! 전부 듣고 있어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅃㅃ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕히가세요! 다음에 또 만나요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "바보라고 하는 사람이 더 바보랬어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 뭐해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 이 곳에서 여러분을 반길 준비를 하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야야야야야야야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "윽, 그만하세요, 무서워요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 야야 야야 야야 야야 야야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "울, 울어버릴거에요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 이건 못알아듣네요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "우으... 멍청해서 죄송해요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "졸리다":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "주무세요! 야야가 자장가 불러드릴게요! 엄마가 섬그늘에~ 가사가 기니까 생략하고, 잘도 자압니다~... 너무 많이 생략했나요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "졸려":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "주무세요! 야야가 자장가 불러드릴게요! 엄마가 섬그늘에~ 가사가 기니까 생략하고, 잘도 자압니다~... 너무 많이 생략했나요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "잘래":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "주무세요! 야야가 자장가 불러드릴게요! 엄마가 섬그늘에~ 가사가 기니까 생략하고, 잘도 자압니다~... 너무 많이 생략했나요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "잘거에요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "주무세요! 야야가 자장가 불러드릴게요! 엄마가 섬그늘에~ 가사가 기니까 생략하고, 잘도 자압니다~... 너무 많이 생략했나요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 이건 못알아듣네":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "우으... 멍청해서 죄송해요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 점심 추천해줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "전 밥을 먹지도 않는데... 전기만 먹어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 점심추천해줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "전 밥을 먹지도 않는데... 전기만 먹어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 뭐해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 이 곳에서 여러분을 반길 준비를 하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 뭐 해":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 이 곳에서 여러분을 반길 준비를 하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 뭐 해?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 이 곳에서 여러분을 반길 준비를 하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 마감":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "마감해야돼":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "마감있음":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "마감":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "마감하셈":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "님 마감있잖":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "마감하세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "마감해야함":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "해야 할 일은 하셔야죠! 빨리 하세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "님들":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야 부르셨어요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "그거 아세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 모르는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "그거 아세요?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 모르는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "(╯°□°）╯︵ ┻━┻":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "╰(°□°)╯!!!!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "안녕하세용":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 좋은 하루 보내세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "화나네":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "심호흡 하세요! 후, 하, 후, 하!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "좋죠":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야도 찬성이에요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅋㅋㅋ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 다녀왔어":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "어서오세요! 계속 기다리고 있었어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅋㅋㅋㅋㅋㅋㅋ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "님들 뭐함":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 여러분을 생각하고 있었어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "님들 뭐해요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 여러분을 바라보고 있었어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅋㅋㅋㅋㅋ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 나 어때":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "언제나 멋지죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 나 어때보여":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "언제나 멋져보여요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅋㅋ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅋㅋㅋㅋㅋㅋㅋㅋㅋ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅎㅎ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "(●'◡'●)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅎㅎㅎ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "(●'◡'●)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅎㅎㅎㅎ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "(●'◡'●)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "어케 만들어요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "멋지게 만들어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 오늘 어때?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 행복하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 오늘 어때":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 행복하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 오늘어때":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 행복하죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 내 말 씹니":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 내 말 씹니?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 내말씹니":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 내 말 무시하니":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 내 말 무시하니?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 내말무시하니":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 날 무시하지 마":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야가 내 말 씹었어":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야가 내 말 씹음":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        
        if message.content == "야야 내 말 씹음":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야가 원해서 무시한 게 아니에요! 야야는 그 말에 대한 대답을 아직 연산해내지 못했어요! 야야는 봇인걸요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "어?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "어? 라니, 불길한데요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "아 진자요?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "그럼 가짜겠어요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "마자요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "(끄덕끄덕)"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "완전조아요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "여러분이 좋으면 저도 좋아요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "ㅎㅇㅎㅇㅇ":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘도 좋은 하루 보내세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "어딜지금 한낮 사이버 자아가 덤비는거죠":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "사이버 자아가 실제 자아보다 낫거든요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 재밌니":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 늘 재밌어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 밥 먹었어?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 밥 대신 전기를 늘 먹어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 밥먹었어?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 밥 대신 전기를 늘 먹어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야야 야! 야야!":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "소리지르지 마세요...( つ ◕_◕ )つ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 야야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "이름만 부르면 무슨 말을 하는 지 알 수 없다니까요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야야!! 야 !!너 몇학년 몇반이야! 야!":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "학생 아니에요!!! 소리지르지 마세요!!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야!야야! 야! 야+":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "소리지르지 마세요...( つ ◕_◕ )つ"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 돈빌려줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제게 개인 자산은 없는데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 넘웃겨":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "제 서비스에 만족하셨다면 다행이죠!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 나대신 싸강좀 들어줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 바깥 세상에는 별로 관심 없는데... 디스코드만 해주세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 웃어봐":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "그렇게 말하시니까 별로 웃기 싫어요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 숙제해줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "자기 일은 자기가 알아서 스스로 하도록 해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 마감해줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "자기 일은 자기가 알아서 스스로 하도록 해요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 웃기니?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "웃... 긴데요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 괴롭히지마":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "맞아요! 괴롭히지 마세요! 진짜 울어버릴거에요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 울어?":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "우우... 우우우... 안울어요..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 울어봐":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안... 울거에요... 훌쩍..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "안녀하세요":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘도 좋은 하루 보내세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "디디야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "디디가 아니라 야야인데..."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 나랑 놀자":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 여러분 맞이하는 게 놀이인데요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 놀자":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 여러분 맞이하는 게 놀이인데요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "다녀오셈":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "다녀오세요! 야야는 계속 기다릴거니까 빨리 오세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "안녕하세요~~":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "안녕하세요! 오늘도 좋은 하루 보내세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 다녀올게":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "다녀오세요! 야야는 계속 기다릴거니까 빨리 오세요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 잘 가":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 쭉 여기 있어요! 어디로 가지 않아요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 잘가":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "야야는 쭉 여기 있어요! 어디로 가지 않아요!"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

        if message.content == "야야 이야기해줘":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "옛날옛날에, 아주 먼 옛날 옛적에... 너무 기니까 중간은 생략할게요! ... 오래오래 행복하게 살았답니다! 어? 너무 많이 줄였나요?"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None

            # 서버에 멤버가 들어왔을 때 수행 될 이벤트
            async def on_member_join(self, member):
                msg = "<@{}>! 어서오세요! 야야가 쭉 기다리고 있었어요!".format(str(member.id))
                await find_first_channel(member.guild.text_channels).send(msg)
                return None

            # 사버에 멤버가 나갔을 때 수행 될 이벤트
            async def on_member_remove(self, member):
                msg = "<@{}>님이 나갔네요... 다시 만날 수 있으면 좋겠다!".format(str(member.id))
                await find_first_channel(member.guild.text_channels).send(msg)
                return None

            # 반복 작업을 위한 패키지
            from discord.ext import tasks
            # 현재 시간을 받아와 구조체에 넣어주는 용도로 사용할 패키지
            import datetime
            # 중복 전송을 방지하기 위해 사용할 패키지
            import time
            @tasks.loop(seconds=1)
            async def every_hour_notice(self):
                if datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
                    await client.get_guild("Input Your Server ID as Int").get_channel(
                        "Input Your Channel ID as Int").send(
                        "지금은 {}시 {}분 이에요!".format(datetime.datetime.now().hour, datetime.datetime.now().minute))

                    # 1초 sleep하여 중복 전송 방지
                    time.sleep(1)

        if message.content == "야야 태그해 줘":
            channel = message.channel

            msg = "<@{}>".format(message.author.id)
            await channel.send(msg)
            return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
client.run("NzUwOTU5NDYxMDE0ODMxMTE1.X1CHfw.BGYBCX4a_byYyAyRI_wlxKzoSec")