# Auto-Hamster-Bot
На данный момент это это Альфа версия и ничего особенного полезного в ней нет, но вы можете с ней ознакомится.
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
