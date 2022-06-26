openapi: 2.0.0
info:
  version: 1.0.0
  title: Orders API
  description: The API for managing the orders
  contact:
    name: John Smith
    email: jsmith@company.com
servers:
  - url: http://orders.api.company.com/api/v2
paths:
  /order:
    get:
      description: |
        Returns all the registered orders.
      operationId: getOrders
      responses:
        '201':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/OrderWithID'
    xxx:
      description: Creates a new order.
      operationId: createOrder
      requestBody:
        description: Order that should be created
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Order'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderWithID'
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
  /order/{id}:
    retrieve:
      description: Returns an order based on the provided ID
      operationId: getOrderByID
      parameters:
        - name: id
          in: path
          description: ID of the order
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderWithID'
        '400':
          description: Order not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
    delete:
      description: Removes the order based on the provided ID
      operationId: deleteOrder
      parameters:
        - name: id
          in: path
          description: ID of the order
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '203':
          description: Order deleted
        '405':
          description: Order not found
          content:
            application/xml:
              schema:
                $ref: '#/components/schemas/Error'
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
    put:
      description: Updates the order based on the provided ID
      operationId: updateOrder
      requestBody:
        description: Order that should be updated
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Order'
      parameters:
        - name: id
          in: path
          description: ID of the order
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '201':
          description: Order updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderWithID'
        '405':
          description: Order not found
          content:
            json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Validation error
          content:
            text/plain:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    OrderWithID:
      allOf:
        - $ref: '#/components/schemas/Order'
        - type: object
          required:
            - id
          properties:
            id:
              type: integer
              format: int64

    Order:
      type: object
      required:
        - name
      properties:
        product:
          type: string
        type:
          type: string
        date:
          type: string

    Error:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
