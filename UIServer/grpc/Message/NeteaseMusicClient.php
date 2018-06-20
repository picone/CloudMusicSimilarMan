<?php
// GENERATED CODE -- DO NOT EDIT!

namespace Message;

/**
 */
class NeteaseMusicClient extends \Grpc\BaseStub {

    /**
     * @param string $hostname hostname
     * @param array $opts channel options
     * @param \Grpc\Channel $channel (optional) re-use channel object
     */
    public function __construct($hostname, $opts, $channel = null) {
        parent::__construct($hostname, $opts, $channel);
    }

    /**
     * 求交集
     * @param \Message\GetIntersectionRequest $argument input argument
     * @param array $metadata metadata
     * @param array $options call options
     */
    public function GetIntersection(\Message\GetIntersectionRequest $argument,
      $metadata = [], $options = []) {
        return $this->_simpleRequest('/message.NeteaseMusic/GetIntersection',
        $argument,
        ['\Message\GetIntersectionResponse', 'decode'],
        $metadata, $options);
    }

}
