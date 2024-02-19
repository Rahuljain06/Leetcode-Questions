class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = list(range(n))
        heapify(free_rooms)
        meetings_info = [] # [endtime,room]
        num_rooms = [0] * n
        for start, end in sorted(meetings):
            while meetings_info and meetings_info[0][0] <= start:
                _, room_number = heappop(meetings_info)
                heappush(free_rooms, room_number)
            if not free_rooms:
                end_time, room = heappop(meetings_info)
                end=end_time+end-start
                heappush(free_rooms,room)
            room=heappop(free_rooms)
            heappush(meetings_info,(end,room))
            num_rooms[room] += 1

        return num_rooms.index(max(num_rooms))