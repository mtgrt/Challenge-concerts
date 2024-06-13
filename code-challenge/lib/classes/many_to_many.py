
class Band:
    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown
        self._concerts = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def hometown(self):
        return self._hometown
    
    def concerts(self):
        return self._concerts
    
    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise TypeError("Must add an instance of Concert")
    
    def venues(self):
        return list(set(concert.venue for concert in self._concerts))
    
    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self.add_concert(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]
class Concert:
    def __init__(self, date, band, venue):
        self._date = date
        self._band = band
        self._venue = venue
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")
    
    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise TypeError("Must be an instance of Band")
    
    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise TypeError("Must be an instance of Venue")
    
    def hometown_show(self):
        return self._venue.city == self._band.hometown
    
    def introduction(self):
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"
class Venue:
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._concerts = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")
    
    def concerts(self):
        return self._concerts
    
    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise TypeError("Must add an instance of Concert")
    
    def bands(self):
        return list(set(concert.band for concert in self._concerts))
