### Описание:
**Auto-Hamster-Bot** — это программа, предназначенная для автоматизации улучшения карточек в популярной игре **Hamster Kombat**. Программа предоставляет пользователю возможность улучшать карточки быстрее и эффективнее, а также управлять несколькими аккаунтами одновременно.
**Улучшение карточек**:
   - Автоматизирует процесс улучшения карточек.
   - Поддерживает оптимизацию процесса улучшения, минимизируя затраты времени и ресурсов.
**Работа с несколькими аккаунтами**:
   - Поддержка мульти-аккаунтов для одновременного улучшения карточек на разных профилях.

В начале вам стоит ознакомится с этим роликом 
https://youtu.be/PTdUmkT-yas?si=rM84Y8TGteJF-1LA

---
## Код из видео

```js
{
    const original_indexOf = Array.prototype.indexOf
    Array.prototype.indexOf = function (...args) {
        if(JSON.stringify(this) === JSON.stringify(["android", "android_x", "ios"])) {
            setTimeout(() => {
                Array.prototype.indexOf = original_indexOf
            })
            return 0
        }
        return original_indexOf.apply(this, args)
    }
}
```

![image](https://imgur.com/h1IhPqh.png)
Значение "Authorization" копируем и вставляем в conf.py
