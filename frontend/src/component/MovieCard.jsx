import { Card } from 'antd';
import React from 'react';

export function MovieListCard(movieData) {
    movieData = movieData.movieData
    const {name, actor,genres,director} = movieData;
    return(
        <>
            <Card title={`Title: ${name}`} extra={<a href="#">More</a>} style={{ width: 300 }}>
                <p>Name: {`${actor}`}</p>
                <p>Genres: {`${genres}`}</p>
                <p>Director: {`${director}`}</p>
            </Card>
        </>
    )
}
