class Card:
	def __init__(self, id, name, cooldownSeconds, price, profitPerHourDelta, isAvailable, isExpired,
	             profitPerHour, condition, section, level, currentProfitPerHour, totalCooldownSeconds, maxLevel=None,
	             toggle=None, expiresAt=None):
		self._maxLevel = maxLevel
		self._id = id
		self._name = name
		self._cooldownSeconds = cooldownSeconds
		self._price = price
		self._profitPerHourDelta = profitPerHourDelta
		self._isAvailable = isAvailable
		self._isExpired = isExpired
		self._profit = price / profitPerHourDelta
		self._profitPerHour = profitPerHour
		self._condition = condition
		self._section = section
		self._level = level
		self._currentProfitPerHour = currentProfitPerHour
		self._totalCooldownSeconds = totalCooldownSeconds

	# Геттеры
	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def get_cooldownSeconds(self):
		return self._cooldownSeconds

	def get_price(self):
		return self._price

	def get_profitPerHourDelta(self):
		return self._profitPerHourDelta

	def get_isAvailable(self):
		return self._isAvailable

	def get_isExpired(self):
		return self._isExpired

	def get_profit(self):
		return self._profit

	def get_profitPerHour(self):
		return self._profitPerHour

	def get_condition(self):
		return self._condition

	def get_section(self):
		return self._section

	def get_level(self):
		return self._level

	def get_currentProfitPerHour(self):
		return self._currentProfitPerHour

	def get_totalCooldownSeconds(self):
		return self._totalCooldownSeconds

	def get_maxLevel(self):
		return self._maxLevel

	# Сеттеры
	def set_id(self, id):
		self._id = id

	def set_name(self, name):
		self._name = name

	def set_cooldownSeconds(self, cooldownSeconds):
		self._cooldownSeconds = cooldownSeconds

	def set_price(self, price):
		self._price = price
		self._profit = price / self._profitPerHourDelta  # обновление profit при изменении цены

	def set_profitPerHourDelta(self, profitPerHourDelta):
		self._profitPerHourDelta = profitPerHourDelta
		self._profit = self._price / profitPerHourDelta  # обновление profit при изменении delta

	def set_isAvailable(self, isAvailable):
		self._isAvailable = isAvailable

	def set_isExpired(self, isExpired):
		self._isExpired = isExpired

	def set_profitPerHour(self, profitPerHour):
		self._profitPerHour = profitPerHour

	def set_condition(self, condition):
		self._condition = condition

	def set_section(self, section):
		self._section = section

	def set_level(self, level):
		self._level = level

	def set_currentProfitPerHour(self, currentProfitPerHour):
		self._currentProfitPerHour = currentProfitPerHour

	def set_totalCooldownSeconds(self, totalCooldownSeconds):
		self._totalCooldownSeconds = totalCooldownSeconds

	def set_maxLevel(self, maxLevel):
		self._maxLevel = maxLevel
