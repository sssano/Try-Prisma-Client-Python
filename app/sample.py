import asyncio
from datetime import datetime
from contextlib import asynccontextmanager
from prisma import Prisma

prisma = Prisma()


@asynccontextmanager
async def connection():
    await prisma.connect()
    yield
    await prisma.disconnect()


async def main() -> None:
    async with connection():
        now = datetime.now().timestamp()
        user = await prisma.user.create(
            data={
                'name': 'sample',
                'email': f'{now}@example.com',
                'posts': {
                    'create': {
                        'title': 'Include this post!',
                        'content': 'prisma',
                    },
                },
            },
            include={
                'posts': True,
            }
        )
        print(user)

        posts = await prisma.post.find_many(
            where={
                'OR': [
                    {'title': {'contains': 'prisma'}},
                    {'content': {'contains': 'prisma'}},
                ]
            }
        )
        print(posts)

        post = await prisma.post.update(
            where={
                'id': 1,
            },
            data={
                'views': {
                    'increment': 1,
                },
            },
        )
        print(post)


if __name__ == '__main__':
    asyncio.run(main())
