from openai import OpenAI

# Possible to encrease spead by collapsing querries
def ai_request(simptoms):
    '''
    Request to an AI to define disease.
    Returns dict of lists with keys: disease_category & description.
    '''
    client = OpenAI(
        api_key="sk-AJIPtiFlPxvPvao2TYREAV99wEJHKoEq",
        base_url="https://api.proxyapi.ru/openai/v1",
        # base_url="https://api.openai.com/v1",
    )

    completion_disease = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Выведи наиболее вероятную болезнь или несколько болезненей (но не более 3х), разделив их только запятыми по следующим симптомам в квадратных скобках:[ {simptoms} ]. В твоем сообщении должны быть только названия болезней. Без точки в конце",
            }
        ]
    )

    disease_category = completion_disease.choices[0].message.content.split(sep=",")

    completion_description = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Расскажи про каждую болезнь из этого списка: {disease_category}. На описание каждой болезни примерно 90-110 слов. Пиши в научном формате. Каждый текст раздели знаком ';'. В конце без точки. В твоем сообщении должны быть только описания на все болезни. В последнем предложении напиши медицинскую специализацию, которая занимается лечением этого недуга."
            }
        ]
    )

    description = completion_description.choices[0].message.content.split(sep=";")

    return {
        'disease_category': disease_category,
        'description': description,
    }



def main():
    pass

if __name__ == '__main__':
    main()