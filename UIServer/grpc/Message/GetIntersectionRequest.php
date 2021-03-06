<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

namespace Message;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>message.GetIntersectionRequest</code>
 */
class GetIntersectionRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>repeated uint64 song_ids = 1;</code>
     */
    private $song_ids;
    /**
     * Generated from protobuf field <code>int32 limit = 2;</code>
     */
    private $limit = 0;

    public function __construct() {
        \GPBMetadata\Service::initOnce();
        parent::__construct();
    }

    /**
     * Generated from protobuf field <code>repeated uint64 song_ids = 1;</code>
     * @return \Google\Protobuf\Internal\RepeatedField
     */
    public function getSongIds()
    {
        return $this->song_ids;
    }

    /**
     * Generated from protobuf field <code>repeated uint64 song_ids = 1;</code>
     * @param int[]|string[]|\Google\Protobuf\Internal\RepeatedField $var
     * @return $this
     */
    public function setSongIds($var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::UINT64);
        $this->song_ids = $arr;

        return $this;
    }

    /**
     * Generated from protobuf field <code>int32 limit = 2;</code>
     * @return int
     */
    public function getLimit()
    {
        return $this->limit;
    }

    /**
     * Generated from protobuf field <code>int32 limit = 2;</code>
     * @param int $var
     * @return $this
     */
    public function setLimit($var)
    {
        GPBUtil::checkInt32($var);
        $this->limit = $var;

        return $this;
    }

}

