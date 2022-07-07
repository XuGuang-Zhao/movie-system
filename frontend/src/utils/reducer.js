import React, { createContext } from 'react';

export const reducer = (state, action) => {
    switch (action.type) {
        case 'userID':
            return {
                ...state,
                userID: action.userID,
            };
        default:
            throw new Error();
    }
}


export const UserContext = createContext({});
