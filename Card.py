class Card:
    class Card:
        def __init__(self, card_id, card_name, card_cooldown, card_price, card_profit_per_hour_delta, card_is_available,
                     card_is_expired):
            self.card_is_expired = card_is_expired
            self.card_is_available = card_is_available
            self.card_id = card_id
            self.card_name = card_name
            self.card_cooldown = card_cooldown
            self.price = card_price
            self.profit_per_hour_delta = card_profit_per_hour_delta
            self.profit = self.price / self.profit_per_hour_delta

        def __repr__(self):
            return f"Student(card_name={self.card_name}, price={self.price}, card_cooldown={self.card_cooldown})"

        # Геттер для card_is_expired
        @property
        def card_is_expired(self):
            return self._card_is_expired

        # Геттер для card_is_available
        @property
        def card_is_available(self):
            return self._card_is_available

        # Геттер для card_id
        @property
        def card_id(self):
            return self._card_id

        # Геттер для card_name
        @property
        def card_name(self):
            return self._card_name

        # Геттер для cooldown
        @property
        def card_cooldown(self):
            return self._cooldown

        # Геттер для price
        @property
        def price(self):
            return self._price

        # Геттер для profit_per_hour_delta
        @property
        def profit_per_hour_delta(self):
            return self._profit_per_hour_delta

        # Геттер для profit
        @property
        def profit(self):
            return self._profit

        # Теперь используем приватные атрибуты с нижним подчёркиванием
        @card_is_expired.setter
        def card_is_expired(self, value):
            self._card_is_expired = value

        @card_is_available.setter
        def card_is_available(self, value):
            self._card_is_available = value

        @card_id.setter
        def card_id(self, value):
            self._card_id = value

        @card_name.setter
        def card_name(self, value):
            self._card_name = value

        @card_cooldown.setter
        def card_cooldown(self, value):
            self._cooldown = value

        @price.setter
        def price(self, value):
            self._price = value

        @profit_per_hour_delta.setter
        def profit_per_hour_delta(self, value):
            self._profit_per_hour_delta = value

        @profit.setter
        def profit(self, value):
            self._profit = value
