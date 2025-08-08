"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
          self.last_name = last_name
          self._members = [
        {"first_name": "Tommy", "id": 3443, "age": 23, "lucky_numbers": [34, 65, 23, 4, 6]},
        {"first_name": "Yeimy", "id": 2222, "age": 28, "lucky_numbers": [7, 13, 22]},
        {"first_name": "Albania", "id": 3333, "age": 30, "lucky_numbers": [10, 14, 3]}
    ]
          self._next_id = max(m['id'] for m in self._members) + 1


    # This method generates a unique incremental ID
    def _generate_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_member(self, member):
        # Assign an id if member doesn't have one
        if "id" not in member or member["id"] is None:
            member["id"] = self._generate_id()
        # Add last_name if missing, set to family's last_name
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    
    def get_all_members(self):
        return self._members