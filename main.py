from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, ShareEvent, LikeEvent, FollowEvent, ViewerUpdateEvent

client: TikTokLiveClient = TikTokLiveClient(
    unique_id = "yo.meli", **(
        {
            "fetch_room_info_on_connect": True,
        }
    )
)

@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

@client.on("comment")
async def on_connect(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1 and event.gift.repeat_end == 1:
        print(f"{event.user.uniqueId} sent {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"")

    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        print(f"{event.user.uniqueId} sent \"{event.gift.extended_gift.name}\"")

@client.on("like")
async def on_like(event: LikeEvent):
    print(f"{event.user.unique_id} has liked the stream!")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.unique_id} followed the streamer!")

@client.on("share")
async def on_share(event: ShareEvent):
    print(f"{event.user.unique_id} shared the streamer!")

@client.on("viewer_count_update")
async def on_connect(event: ViewerUpdateEvent):
    print("Received a new viewer count", event.ViewerUpdate)

if __name__ == '__main__':
    client.run()