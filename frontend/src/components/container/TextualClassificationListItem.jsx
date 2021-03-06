// @flow
import React, {Component} from "react";
import ListGroup from "react-bootstrap/ListGroup";
import {Link} from "react-router-dom";
import {LinkContainer} from "react-router-bootstrap";

type Props = {
    item: Object
}

export default class TextualClassificationListItem extends Component<Props> {
    render() {
        const {id, name} = this.props.item;
        const toUrl = `/textual_classification/${id}/`;

        return (
            <LinkContainer to={toUrl}>
                <ListGroup.Item className="d-sm-flex justify-content-sm-between cursor-pointer">
                    <div>
                        <p className="m-0"><strong>{name}</strong></p>
                    </div>
                    <div className="pt-2 pb-1 py-sm-0 pl-sm-3">
                        <Link to={toUrl} className="btn btn-xs btn-info">Editar</Link>
                    </div>
                </ListGroup.Item>
            </LinkContainer>
        )
    }
}
