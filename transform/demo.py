import torch

from gpt import GPT

if __name__ == '__main__':
    # device = torch.device('cuda')
    device = torch.device('cpu')
    model = GPT().to(device)
    model.load_state_dict(torch.load('GPT2.pt'))

    model.eval()
    #初始输入是空，每次加上后面的对话信息
    sentence = ''
    while True:
        temp_sentence = input("我:")
        sentence += (temp_sentence + '\t')
        if len(sentence) > 200:
            #由于该模型输入最大长度为300，避免长度超出限制长度过长需要进行裁剪
            t_index = sentence.find('\t')
            sentence = sentence[t_index + 1:]

        print("sentense:", sentence)
        answer = model.answer(sentence)
        # sentence += (answer + '\t')
        print("机器人:", answer)
