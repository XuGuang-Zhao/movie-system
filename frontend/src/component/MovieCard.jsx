/* eslint-disable jsx-a11y/alt-text */
import { Card, Rate } from 'antd';
import React from 'react';

export default function MovieCard(movieData) {
    const { id, name, actor, genres, director, image, rating } = movieData?.movieData;
    // TODO: JUMP TO MOVIE INFO
    const jumpToMovie = (id) => {
        console.log(id);
    }
    return (
        <>
            <Card
                hoverable
                title={`${name}`}
                style={{ width: 250 }}
                cover={<img src={image} style={{ height: 300 }} />}
                onClick={() => jumpToMovie(id)}
            >
                <p>Genres: {`${genres}`}</p>
                <p>Director: {`${director}`}</p>
                <p>Actors: {`${actor}`}</p>
                <p>Rate: {`${rating}`} <Rate allowHalf disabled value={rating / 2} /> </p>
            </Card>
        </>
    )
}
