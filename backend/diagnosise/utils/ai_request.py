from openai import OpenAI

# Possible to encrease spead by collapsing querries
def ai_request(symptoms):
    '''
    Request to an AI to define disease.
    Returns dict of lists with keys: disease_category & description.
    '''
    client = OpenAI(
        api_key="api_key",
        base_url="models_url",
    )

    completion_disease = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Output the most likely disease or several diseases (but no more than 3), separated only by commas, based on the following symptoms in square brackets: [ {symptoms} ]. Your response should contain only the names of diseases. If instead of symptoms or a description of health conditions there is something else, reply: 'error'. Without a period at the end",
                # "content": f"Выведи наиболее вероятную болезнь или несколько болезненей (но не более 3х), разделив их только запятыми по следующим симптомам в квадратных скобках:[ {symptoms} ]. В твоем сообщении должны быть только названия болезней. Если вместо симптомов или описания состояния здоровья что-то другое, ответь: 'ошибка'. Без точки в конце",
            }
        ]
    )

    disease_category = completion_disease.choices[0].message.content.split(sep=",")

    completion_description = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Describe each disease from this list inside square brackets: [{disease_category}]. Provide approximately 90-110 words for each description. Write in a scientific format. Primarily describe the progression and consequences of the disease, as well as treatment methods. In the last sentence, mention the doctor who specializes in this disease. Separate each text with the '$' symbol. Without a period at the end. Your response should contain only descriptions for all diseases. If there is something other than diseases inside '[]', reply: 'error'.",
                # "content": f"Расскажи про каждую болезнь из этого списка внутри квадратных скобок: [{disease_category}].  На описание каждой болезни примерно 90-110 слов. Пиши в научном формате. В основном расскажи о протекании и последствиях заболевания, а также о методах лечения. В последнем предложении назови врача, который занимается этой болезнью. Каждый текст раздели знаком '$'. В конце без точки. В твоем сообщении должны быть только описания на все болезни. Если вместо болезней внутри '[]' что-то другое, ответь: 'ошибка'.",
            }
        ]
    )

    description = completion_description.choices[0].message.content.split(sep="$")

    return {
        'disease_category': disease_category,
        'description': description,
    }



def main():
    pass

if __name__ == '__main__':
    main()