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

// --- Нас итересует только то что выше


{

    const button = document.querySelector(".user-tap-button")
    let reachedZeroEnergy = false
    function tick() {
        try {
            const energy = document.querySelector(".user-tap-energy > p")
            if(energy) {
                const energyStr = energy.innerText
                const currEnergy = Number(energyStr.split('/')[0])
                const maxEnergy = Number(energyStr.split('/')[1])
                
                if(!reachedZeroEnergy) {
                    button.dispatchEvent(new PointerEvent('pointerup'))
                    button.dispatchEvent(new PointerEvent('pointerup'))
                    button.dispatchEvent(new PointerEvent('pointerup'))
                    button.dispatchEvent(new PointerEvent('pointerup'))
                }
                if(currEnergy <= 10) {
                    reachedZeroEnergy = true
                }
                if(currEnergy >= maxEnergy - 10) {
                    reachedZeroEnergy = false
                }
            }
        } catch(e) {
            console.log(e)
        }
        
        setTimeout(tick, 100 * Math.random() + 50)
    }
    tick()
}
```

![image](https://imgur.com/h1IhPqh.png)
Значение "Authorization" копируем и вставляем в conf.py
