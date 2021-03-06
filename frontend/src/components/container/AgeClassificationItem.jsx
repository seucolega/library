// @flow
import React, {Component} from "react";
import PageHeader from "../presentational/PageHeader";
import AgeClassificationItemForm from "./AgeClassificationItemForm";
import {API_URL, fetchHeaders} from "../../App";

type Props = {
    id: number
}

type State = {
    item: Object,
    isLoading: boolean,
    error: void | Object
}

export default class AgeClassificationItem extends Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {
            item: null,
            isLoading: true,
            error: null
        };
    }

    componentDidMount() {
        fetch(`${API_URL}/book/age_classification/${this.props.id}/`, {
            headers: fetchHeaders()
        })
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        item: result,
                        isLoading: false,
                        error: result.error
                    });
                },
                (error) => {
                    this.setState({
                        isLoading: false,
                        error: error
                    });
                }
            )
    }

    render() {
        const {error, isLoading, item} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (isLoading) {
            return <div>Loading...</div>;
        } else {
            return (
                <div>
                    <PageHeader title="Editar classificação"/>
                    <AgeClassificationItemForm item={item}/>
                </div>
            );
        }
    }
}